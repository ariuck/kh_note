import seaborn as sns
from sklearn.metrics import accuracy_score, classification_report
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

df = sns.load_dataset("penguins")
df.to_csv("data/penguins.csv")
df = df.dropna().reset_index(drop=True)

# train , test
features = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]
X = df[features]
y = df["species"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    stratify=y,
    random_state=42
)

# 학습
m = LogisticRegression(max_iter=5000)
m.fit(X_train, y_train)

# 예측
y_pred = m.predict(X_test)

# 결과
acc = accuracy_score(y_test, y_pred)
print("accuracy_score : ", acc)

# 혼동행렬
lbs = ["Gentoo" , "Chinstrap", "Adelie"]
cm = confusion_matrix(y_test, y_pred, labels=lbs)
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(data=cm, annot=True, fmt="d", ax=ax, xticklabels=lbs, yticklabels=lbs , cmap="Blues")
plt.xlabel("예측")
plt.ylabel("실제")
plt.show()

result = classification_report(y_test , y_pred , labels=lbs)
print(result)