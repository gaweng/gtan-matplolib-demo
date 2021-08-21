import matplotlib.pyplot as plt
import numpy as np

np.random.seed(48935798)
data = np.random.randn(2, 100)

fig, axs = plt.subplots(2, 2)
axs[0, 0].hist(data[0])
axs[1, 0].scatter(data[0], data[1])
axs[0, 1].plot(data[0], data[1])
axs[1, 1].hist2d(data[0], data[1])

plt.show()

# Pie-Charts
label = ["Typ-1", "Typ-2", "Typ-3"]
value = [3,2,8]

plt.pie(value, labels=label)

plt.show()