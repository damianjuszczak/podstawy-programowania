
# Takes a number from the user and counts down to zero.
#
# Modify the program so that the last five seconds of the countdown
# are displayed in words, i.e. five, four, three, two, one.
import time

words = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five'
}

countdown = int(input('Enter the number of seconds to count down: '))

while countdown > 0:
    # Check if the remaining time is 5 or less.
    if countdown in words:
        # If it is one of the last five, print the word.
        print(words[countdown])
    else:
        # Otherwise, print the number.
        print(countdown)
        
    countdown -= 1
    time.sleep(1)

print("Time's up!")