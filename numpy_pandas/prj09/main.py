import pandas as pd

# 데이터 준비
df = pd.read_csv('data/emp.csv')

# 결측치 확인
print("##### 전처리 전 #####")
print(df.isna().sum())

# 결측치 나이 중위값으로 채우기
df["나이"] = df["나이"].fillna(df["나이"].median())

# 결측치 도시 최빈값으로 채우기
x = df["도시"].mode()[0]
df["도시"] = df["도시"].fillna(x)

# 결측치 연봉 해당 행 없애기
df = df.dropna(subset=["연봉","이름"])

# 중복 제거
df.drop_duplicates(inplace=True)

# 칼럼명 바꾸기 도시 -> 지역
df = df.rename(columns={"도시":"지역"})

# 칼럼 삭제 // 이름 칼럼 삭제
df.drop(columns=["이름"] , inplace=True)

# 나이 칼럼의 타입 int로 변경
df["나이"] = df["나이"].astype("int")
df["연봉"] = df["연봉"].astype("int")

# 값 치환 // 서울 -> 한양
df["지역"] = df["지역"].replace("서울" , "한양")

# 월급 칼럼 만들기 (인트 타입으로)
df["월급"] = (df["연봉"] / 12).astype(int)

# 정렬 , 값 기준
df.sort_values("월급" , ascending=False , inplace=True)

print("@@@@@@@@@@@@@")
print(df.head())

# 정렬 , 인덱스 기준
# df = df.sort_index(axis=1)




# 전처리 이후 데이터 확인
print("\n\n##### 전처리 후 #####")
print(df.head())
