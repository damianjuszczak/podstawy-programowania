def text_analyzer():
    filename = input('File name: ')

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            line_counter = len(lines)
            whole_text = ''.join(lines)
            char_counter = len(whole_text)
            word_counter = len(whole_text.split())

            print(f'File name: {filename}')
            print(f'Number of lines: {line_counter}')
            print(f'Number of characters: {char_counter}')
            print(f'Number of words: {word_counter}')

            

    except FileNotFoundError:
        print('File not found')

text_analyzer()