# time_string(hours, minutes, time_format)

def time_string(hours, minutes, time_format):

    min_str = f'{minutes:02}' #always two digits in minutes

    if time_format == '24':
        return f'{hours:02}:{min_str}'
    elif time_format == '12':
        suffix = 'am' if hours < 12 else 'pm'
        
        if hours == 0:
            hr_str = 12   #midnight
        elif hours > 12:
            hr_str = hours - 12
        else:
            hr_str = hours
            
        return f'{hr_str}:{min_str}{suffix}'

    
#case1
result1 = time_string(15, 38, '24')
print(f'time_string(15, 38, "24") returns: {result1}')
#case2
result2 = time_string(11, 15, '12')
print(f'time_string(11, 15, "12") returns: {result2}')
