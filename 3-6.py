#program that calculates the distance to the horizon from a height given in meters from the keyboard

import math

#observer's height in m
h = float(input("Enter your height in meters: "))

#calculate distance
d = 3.57 * math.sqrt(h)

#window
w = 3.57 * math.sqrt(20)

print(f"When you're standing on a beach, the distance to the horizon is {d:.2f}km. ")
print(f"When you're looking out of hotel window (height = 20 m), the distance to the horizon is {w:.2f}km.")