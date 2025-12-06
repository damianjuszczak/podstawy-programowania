###
# A program that prints a university abbreviation
#   
import re

university = "Krakow University of Economics"

print(university[0]+university[7]+university[21])

'''
abrev = university.split()
print(abrev)

for word in abrev:
    print(word[0])
abbreviation = ''.join(re.findall(r'\b[A-Z].*?\b', university))

print(abbreviation)

'''