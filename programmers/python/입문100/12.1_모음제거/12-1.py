def solution(my_string):
    vowel = 'aeiou'
    return ''.join([char for char in my_string if char not in vowel])
