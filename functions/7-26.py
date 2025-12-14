# returns the given text with all characters separated by a dash sign
#f("Univesity") returns "U-n-i-v-e-r-s-i-t-y"
#f("UE") returns "U-E"
#f("x") returns "x"
#f("") returns ""

def f(text):
    return '-'.join(text)

# --- Testing the function ---
print(f('University')) # Returns "U-n-i-v-e-r-s-i-t-y"
print(f('UE'))         # Returns "U-E"
print(f('x'))          # Returns "x"
print(f(''))           # Returns ""