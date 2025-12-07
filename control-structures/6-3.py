###
# House lighting with three bulbs and two switches
# Checking how many bulbs are illuminating the house
#

#case1
light_switch1 = False
light_switch2 = False
bulbs_on = 0
if light_switch1:
    bulbs_on += 1
if light_switch2:
    bulbs_on += 2

print(f' switch 1: off, switch 2: off, total bulbs: {bulbs_on}')

#case2
light_switch1 = True
light_switch2 = False
bulbs_on = 0

if light_switch1:
    bulbs_on += 1
if light_switch2:
    bulbs_on += 2

print(f' switch 1: on, switch 2: off , total bulbs: {bulbs_on}')

#case3
light_switch1 = False
light_switch2 = True
bulbs_on = 0

if light_switch1:
    bulbs_on += 1
if light_switch2:
    bulbs_on += 1

print(f' switch 1: off, switch 2: on, total bulbs: {bulbs_on}')

#case4

light_switch1 = True
light_switch2 = True
bulbs_on = 0

if light_switch1:
    bulbs_on += 1
if light_switch2:
    bulbs_on += 1

print(f' switch 1: on, switch 2: on , total bulbs: {bulbs_on}')
