#You never get a second chance to make a first impression
#The number of letter 'e': 7


from letter_counter import count_letter

def main():
    sample_text = 'You never get a second chance to make a first impression'
    target_char = 'e'

    result = count_letter(sample_text, target_char)

    print(sample_text)
    print(f'The number of letter "{target_char}": {result}')

if __name__ == '__main__':
    main()