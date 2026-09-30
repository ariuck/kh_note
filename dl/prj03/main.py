from fastapi import FastAPI, Form
from pydantic import BaseModel

app = FastAPI()


class Book(BaseModel):
    title: str
    price: int



@app.post("/book")
def book(title: str = Form(), price: int = Form()):
    if price >= 10000:
        return "good !!!"
    else:
        return "fail..."



@app.post("/login")
def login(id: str = Form(), pw: str = Form()):
    if id == "admin" and pw == "1234":
        return "login ok"
    else:
        return "login fail"

@app.get("/age")
def age(name: str, age: int):
    if age >=20:
        return f" {name}님은 성인입니다"
    else:
        return f"{name}님은 미성년자입니다"

@app.

