import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6, 4))

arr = np.linspace(0, 10, 10)
ax.plot(arr, arr, marker="^", label="y=x", linestyle="--")
ax.plot(arr, arr * 2, marker="o", label="y=2x", linestyle=":")
ax.plot(arr, arr * 3, marker="s", label="y=3x")
ax.legend()
ax.grid(alpha=0.3)

ax.set_xlabel("hello")
ax.set_ylabel("world")
ax.set_title("pythonnnnnn")

plt.savefig("zzz.png")
plt.show()
