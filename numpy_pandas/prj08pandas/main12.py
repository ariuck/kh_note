import pandas as pd

# 데이터 준비
df = pd.read_csv("data/people.csv")

# 칼럼 삭제
df = df.drop(columns=["나이"])

# 칼럼 추가
df["월급"] = df["연봉"] / 12

# 값 치환
df["도시"] = df["도시"].replace("서울","한양")

# 칼럼 이름 변경
df = df.rename(columns={"월급": "급여", "도시": "지역"})

##########
print(df)
