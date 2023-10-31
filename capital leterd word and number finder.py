
import re


def find_capitalized_words_and_digits(input_string):
    
    capitalized_words = re.findall(r'\b[A-Z]\w*', input_string)
    digits = re.findall(r'\b\d+\b', input_string)
    print('Capitalized words: ' + ', '.join(capitalized_words))
    print('Digits: ' + ', '.join(digits))


find_capitalized_words_and_digits(input())
