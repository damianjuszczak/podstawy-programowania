#A number: 7
#Number 7 in the range <2,15>: yes

import in_range

range_start = 2
range_stop = 15

user_input = int(input('A number: '))

validation = in_range.is_in_range(user_input, range_start, range_stop)

if validation:
    result_text = "yes"
else:
    result_text = "no"

print(f'Number {user_input} in the range <{range_start},{range_stop}>: {result_text}')