#f("+-+++-+---") returns True
#f("+-+-+-+-") returns False
#f("+-++-+--") returns False
#f("+-++-++-+---") returns True

def f(detector):
    people = 0
    
    for action in detector:
        if action == '+':
            people += 1
        elif action == '-':
            people -= 1
            
        if people >= 3:
            return True
            
    return False

print(f'f("+-+++-+---")   returns {f("+-+++-+---")}')
print(f'f("+-+-+-+-")     returns {f("+-+-+-+-")}')
print(f'f("+-++-+--")     returns {f("+-++-+--")}')
print(f'f("+-++-++-+---") returns {f("+-++-++-+---")}')