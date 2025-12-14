#acronym 

#f("Internet of Things") returns "IoT"
#f("For Your Information") returns "FYI"
#f("Python") returns "P"

def f(name):
    words = name.split()
    
    result = ''
    
    for word in words:
        first_letter = word[0]
        
        result = result + first_letter
        
    return result

print(f('Internet of Things'))
print(f('For Your Information'))  
print(f('Python'))                