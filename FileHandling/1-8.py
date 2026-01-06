total_words = 0

with open('pets.txt', 'r') as file:
    for line in file:
        words_in_line = line.split()
        number_of_words = len(words_in_line)
        
        total_words += number_of_words

print(f'Total number of words: {total_words}')