# Boolean Indexing
import pandas as pd

df = pd.read_csv("data/people.csv")

mask = df["나이"].between(30,39)
print(df[mask])

