import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

x = np.linspace(1, 2, 10)
y = x * 2

fig, ax = plt.subplots(figsize=(8, 6))

ax.plot(x, y, marker="o", markersize=15, color="red", linewidth="15", alpha=0.5)
ax.set_title("차트ㅋㅋㅋ", fontweight="bold", fontsize="20")
ax.set_xlabel("엑스으")
ax.set_ylabel("와아이")

# ax.set_ylim(0,10)
# ax.set_yticks([-3,0,10])

ax.annotate("여기보세요", xy=(1.9, 4), xytext=(1.5, 4.0), arrowprops=dict(arrowstyle="->", color="red"))

plt.show()
