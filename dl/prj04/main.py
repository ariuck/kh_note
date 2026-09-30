from fastapi import FastAPI, Response
from fastapi.encoders import jsonable_encoder
from starlette.responses import RedirectResponse, HTMLResponse, FileResponse
from fastapi.responses import JSONResponse
app = FastAPI()

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age


@app.get("/f1")
def f01():
    print("f01 called~~")
    x = Person("hong", 20)
    return RedirectResponse("f2",)

@app.get("/f2")
def f02():
    print("f02 called ...")
    return "f02 의 응답"

@app.get("/f3")
def f03():
    print("f03 called ...")
    return HTMLResponse("<h1>hello world</h1>")

@app.get("/f4")
def f04():
    print("f04 called ...")
    return Response(
        status_code=200,
        headers={
            "atk":"150",
            "speed":"250",
            "nickname":"fdfdsf"
        },
        media_type="text/plain",
        content="123하나둘삼넷오",  # body인듯

    )

@app.get("/f5")
def f05():
    print("f05 called ...")
    return JSONResponse(
        status_code=200,
        headers={"dfjlafd":"asdfasfdfafasf"},
        content={
            "x" :100,
            "y": 200,
        }
    )

@app.get("/f6")
def f06():
    print("f06 called ...")
    x = Person("hong", 20)
    return JSONResponse(
        status_code=200,
        headers={},
        content=jsonable_encoder(x)

    )

@app.get("/f7")
def f07():
    print("f07 called ...")
    return FileResponse("test.jpg")

@app.get("/f8")
def f8(nick:str = "guest"):
    print("f8 called ...")
    s= f'''
        <h1>{nick}hello world</h1>
    '''
    return HTMLResponse(s)