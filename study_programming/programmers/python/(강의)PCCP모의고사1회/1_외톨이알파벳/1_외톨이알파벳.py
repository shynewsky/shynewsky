# ChatGPT

def solution(input_string):
    before = '' # 이전 문자
    exist = set() # 존재한 문자
    lonely = set() # 외톨이 문자
    
    for char in input_string:
        # 2회 이상 나타난 알파벳 & 2개 이상 부분
        if char in exist and char != before:
            lonely.add(char)
        exist.add(char)
        before = char
        
    # 외톨이 문자가 없으면
    if not lonely : 
        return 'N'
    
    return ''.join(sorted(lonely))