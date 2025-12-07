#SURVEY
print('SURVEY')

question_1 = input('Are you interested in computer science? (y/n): ') == 'y'
question_2 = input('Do you like playing computer games? (y/n) ') == 'y'
question_3 = input('Do you have an Instagram account? (y/n): ') == 'y'

#SURVEY RESULTS
print('SURVEY RESULTS')

#if question_1:
#    print('Interested in computer science', 'Yes')
#else:
#    print('Interested in computer science', 'No')

#ternary operator
print('Interested in computer science:', 'Yes' if question_1 else 'No')
print('Playing computer games:', 'Yes' if question_2 else 'No')
print('Has an Instagram account:', 'Yes' if question_3 else 'No')


