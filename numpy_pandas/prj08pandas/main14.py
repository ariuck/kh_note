from cmath import nan

import math
import pandas as pd


def check_grade(salary):
    if math.isnan(salary):
        return "결측치"
    elif salary > 6000:
        return "고소득자"
    else:
        return "일반"


# 데이터 준비
df = pd.read_csv("data/people.csv")

result = df["연봉"].map(check_grade)

print(type(result))
print("result : \n", result)
