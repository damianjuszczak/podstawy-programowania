#Enter tree circumference in cm: 120 
#Tree can be cut down: False 

'''
t1 - 160
t2 - 90
t3 - 230
t4 - 120
'''

circumference = int(input("Enter tree circumference in cm: "))

diameter = (circumference / 3.14 ) >= 50

print(f'Tree can be cut down: {diameter}')

