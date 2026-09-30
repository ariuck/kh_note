import io

import cv2
from PIL import Image
from fastapi import FastAPI,Form, UploadFile, File, Response
from pydantic import BaseModel
from ultralytics import YOLO
from pathlib import Path
from fastapi import HTTPException
from pydantic import BaseModel

x = Path(__file__).resolve().parent
app = FastAPI()
model = YOLO("best.pt")
# @app.post("/hello/{num}")
# def hello(num: int , title : str = Form()):
#     print("num:", num)
#     print("title:" , title)
#     return {"num":num, "title":title}

@app.get("/test")
def test():
    print("test called ~~~")
    results = model(
        source="test_images",
        save=True,
        conf=0.5,
        exist_ok=True,
        project=f"{x}/api_prj",
        name="inf"
    )


@app.post("/upload")
def upload(f: UploadFile = File()):
    #방법2
    if f.content_type not in ("image/jpeg", "image/png"):

        raise HTTPException(status_code=400, detail="only image")

    # print(f.content_type)
    # print(f.filename)
    # print(f.headers)
    data = f.file.read()
    print(type(data))
    print(len(data))

    try:
        buffer = io.BytesIO(data)
        img = Image.open(buffer)
        img = img.convert("RGB")
    except:
        raise HTTPException(status_code=400, detail="can not read image")

    print(img)
    img.save("temp.jpg")

    return {
        "filename": f.filename,
        "content_type": f.content_type,
        "bytes": len(data),
        "width": img.width,
        "height": img.height,
    }

class Detection(BaseModel):
    cls_id: int
    cls_name: str
    conf: float | int
    bbox: list[float | int]

class PredictResponse(BaseModel):
    width: int
    height: int
    count: int
    detection_list: list[Detection]



@app.post("/predict/json")
def predict_json(f: UploadFile = File()) -> PredictResponse:
    data = f.file.read()
    buffer = io.BytesIO(data)
    img = Image.open(buffer)
    img = img.convert("RGB")

    results = model(img, verbose=False)
    result = results[0]

    detection_list = []

    a = result.boxes.cls.tolist()
    b = result.boxes.conf.tolist()
    c = result.boxes.xyxy.tolist()

    for cls, conf, box in zip(a, b, c):
        d = Detection(
            cls_id=int(cls),
            cls_name=result.names[int(cls)],
            conf=round(conf, 3),
            bbox=[round(temp, 2) for temp in box],
        )
        detection_list.append(d)

    return PredictResponse(
        width=result.width,
        height=result.height,
        count=result.count,
        detection_list=detection_list,
    )

#이미지를 그대로(통째로) 가져오기(그전에는 json으로 가져왔었음)
@app.post("/predict/image")
def predict_image(f: UploadFile = File()):
    #f->img로 변경
    data = f.file.read()
    buffer = io.BytesIO(data)
    img = Image.open(buffer)
    img = img.convert("RGB")

    results = model(img, verbose=False)
    r = results[0]

    plotted = r.plot()#박스가 그려진 넘파이 배열을 얻을 수 있음

    ok, buf = cv2. imencode(".jpg", plotted) #cv2.imencode(확장자, 배열) 이미지로 인코딩
    #x에는 성공 여부가 들어있고 찐 이미지 배열이 들어가있음(ok = 성공여부, buf(버퍼) = 찐 이미지 배열(넘파이))

    print(type(buf))#버퍼는 타입이 넘파이 패열임 근데 http에서 사용불가능해서 그냥 파이썬 배열로 바꿔줘야함
    # buf.tobytes()#쌩 바이트 배열로 바꿔줌

    #Response() 그냥 넣으면 헤더에 쌩 바이트로 들어가서 이미지라는걸 알려주기 위해 사용
    return Response(
        content=buf.tobytes(),#쌩 바이트 배열로 변환
        media_type="image/jpeg",#안정성을 위해 사용 *jpeg가 원래 본명이다 jpg로 쓰면 안 될 수도 있음
    )
    #이미지로 가져오는 것 보다 json으로 가져오는 경우가 더 많음
    #이유 : 보통 (클라이언트 -> py -> DB -> 프론트엔드 -> 뷰) 하는 경우가 많아서 이미지로 보기보다 json형태로 숫자받아서 DB에 저장하는 경우가 많음
    
    #지금 한게 클라이언트 -> was dl (이제 클라이언트를 크롬 같은 걸로 바꾸면 더 친숙해 지는거임)
