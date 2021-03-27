import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 100)
y = (np.sin(x - 2) ** 2) * (np.e ** (-x ** 2))
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')

plt.show()
