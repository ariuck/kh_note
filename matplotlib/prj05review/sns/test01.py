import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset("titanic")

print(titanic)

fig , axes = plt.subplots(2,2,figsize=(12,10))

result = titanic[["pclass" , "survived" , "fare"]].corr()
sns.pairplot(data=titanic)

plt.show()


