# A function that returns the number of words in the text
# A function that returns an ordered array of words, from longest to shortest
# A function that returns an alphabetically ordered array of words
import MyText

var = 'An apple a day keeps the doctor away'

word_count = MyText.words_counter(var)
longest = MyText.words_length(var)
alphabet = MyText.words_alphabetical(var)

print(f'Text: {var}')
print(f'Number of words: {word_count}')
print(f'Words from the longest: {longest}')
print(f'Words ordered alphabetically: {alphabet}')

