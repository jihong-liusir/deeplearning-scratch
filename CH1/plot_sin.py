import numpy as np
import matplotlib.pyplot as plt

# Generate data
x = np.arange(0, 6, 0.1) # 以0.1为步长生成0到6的数组
y = np.sin(x)

# Create a plot
plt.plot(x, y)
plt.title('Sine Wave')
plt.show()
