import re

text = input('Enter text: ')
vowels = re.findall(r'[aeiouAEIOU]', text)
count = len(vowels)

print(f'number of vowels in the text: {count}')