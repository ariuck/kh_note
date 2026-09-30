'''
df.sort_values("칼럼" , ascending=False , inplace=True)
df.groupby("부서")
df.groupby("부서")["급여"].mean()
df.groupby("부서")["급여"].agg(["mean" , "max", "min"])

map / apply
df["급여"].map(함수)
'''
import pandas as pd
df = pd.DataFrame({
    "이름" : ["원용", "투용", "삼용", "사용", "오용"] ,
    "급여" : [100,200,300,400,500]
})

def f01(abc):
    if abc > 300:
        return abc * 1.1
    else :
        return abc * 1.2

f02 = lambda abc:abc *1.1 if abc > 300 else abc*1.2


sr = df["급여"]
result = sr.map(f01)
print(result)