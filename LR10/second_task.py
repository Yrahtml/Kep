import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-4, 5, 200)
y = 2*pow(x,2)+x-5

plt.plot(x,y , marker="o", label = "y = 2*(x*x)+x-5")

plt.axhline(0, linewidth=0.8)
plt.axvline(0, linewidth=0.8)
plt.title("Формула")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
