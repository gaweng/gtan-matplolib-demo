import matplotlib.pyplot as plt

xAxis = [1,2,3,4,5,6,7,8,9]
yAxis = [23,45,6,67,6,98,90,23,23]

# Plotten
plt.plot(xAxis, yAxis, label="Graph")

# Y-Achse
plt.ylim(0,400)
plt.ylabel("Y-Achse")

# X-Achse
plt.xlim(0,10)
plt.xticks([4,9], [5,10])
plt.xlabel("X-Achse")

# Plot-Konfigurationen
plt.title("Mein Graph")
plt.legend()
plt.grid()
plt.show()