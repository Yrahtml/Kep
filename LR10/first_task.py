import matplotlib.pyplot as plt
import numpy as np

time =[10,30,50,70,80,100,120,180]
speed =[8,3,5,7,10,15,12,20]

plt.plot(time,speed , marker="o", label = "Значення")

plt.title("Швидкість руху")
plt.xlabel("Час")
plt.ylabel("Швидкість")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
