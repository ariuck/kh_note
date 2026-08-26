# loc , iloc
import pandas as pd

df = pd.read_csv("data/people.csv")

result = df.set_index("이름")

print(result.loc["가영"])
print(result.iloc[0])


