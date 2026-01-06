def get_genre(line):
    parts = line.strip().split(',')
    return parts[2]

def append_to_file(filename, data):
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(data)

def main():
    genre_mapping = {
        'Fantasy': 'books_fantasy.txt',
        'Historical': 'books_historical.txt',
        'Romance': 'books_romance.txt',
        'Classic': 'books_classic.txt'
    }

    with open('books.csv', 'r', encoding='utf-8') as source_file:
        next(source_file) 
        
        for line in source_file:
            genre = get_genre(line)
            
            if genre in genre_mapping:
                target_filename = genre_mapping[genre]
                append_to_file(target_filename, line)

    print('Done')

main()