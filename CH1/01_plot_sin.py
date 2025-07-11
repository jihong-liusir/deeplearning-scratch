import numpy as np
import matplotlib.pyplot as plt

# Generate data
x = np.arange(0, 6, 0.1) # Generae data from 0 to 6, with step 0.1
y = np.sin(x)

plt.plot(x, y)
plt.show()