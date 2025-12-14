import matplotlib.pyplot as plt
import math

x = []
y = []

for angle in range(0, 361):
    x.append(angle)
    # Convert degrees to radians: (angle * PI) / 180
    radians = angle * math.pi / 180
    y.append(math.sin(radians))

plt.plot(x, y)
plt.show()