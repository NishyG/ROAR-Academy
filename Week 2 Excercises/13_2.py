import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1.0, 3.5)

y1 = 2*(x)

y2 = -3*(x)+10
plt.plot(x, y1, color = "blue", linewidth = 1)

plt.plot(x, y2, color = "blue", linewidth = 1)
plt.plot(x, y1, color = "blue", linewidth = 1)
plt.ylim(1, 4)
plt.xlim(1, 3.0)
plt.xticks(np.arange(1, 3.5, 0.5), ["1.0", "1.5", "2.0", "2.5", "3.0"])
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Sample Graph!")
plt.show()