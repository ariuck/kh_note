'''
df = pd.read_csv(파일명)
df = pd.read_excel(파일명)
df.to_csv(파일명 , index = False , encoding = 'utf-8-sig')))

head
tail
shape
info
describe
columns
dtypes

df["칼럼명"]
df[["칼러명", "컬럼명"]]
loc
iloc

df.loc[행, 열]
df.ㅑloc[행,열]

sr = df["age"]
sr > 20
df[bool_arr]
'''