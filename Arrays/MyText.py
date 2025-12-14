# MyText.py

# A function that returns the number of words in the text
def words_counter(text):
    words = text.split()
    return len(words)

# A function that returns an ordered array of words, from longest to shortest
def words_length(text):
    words = text.split()
    words.sort(key=len, reverse=True)
    return words

# A function that returns an alphabetically ordered array of words
def words_alphabetical(text):
    words = text.split()
    words.sort(key=str.lower)
    return words