#car speed, if exceeded
#=>40 & =>140

car_speed = int(input('Enter car speed in km/h e.g. 120: '))
speed_limit_min = 40
speed_limit_max = 140

if car_speed < speed_limit_min or car_speed > speed_limit_max:
    print('Warning: invalid car speed!!')
else:
    print('Speed ok')