#24h time convert to 12h time

#(hh:mm) is read from the keyboard. Sample result:

#Enter time (24-hour format): 16:32
#Time in 12-hour format: 4:32pm

time24 = input('Enter time in 24h format (hh:mm): ')

hour24, minute24 = time24.split(':')
hour12 = int(hour24)

meridiem = 'am'
if hour12 >= 12:
    meridiem = 'pm'
    if hour12 > 12:
        hour12 -= 12

if hour12 == 0:  #midnight
    hour12 = 12

print(f'Time in 12-hour format: {hour12}:{minute24}{meridiem}')