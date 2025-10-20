def solution(new_id):
    print(new_id)
    
    # 1. 모두 소문자
    str1 = new_id.lower()
    print(str1)
    
    # 2. 숫자, 빼기, 밑줄, 마침표 외 제거
    # - isalnum() : a-z, A-Z, 0-9
    # - isalpha() : a-z, A-Z
    str2 = ''                 
    for c in str1:            
        if c.isalnum() or c in '-_.':
            str2 += c            
    print(str2)
    
    # 3. '.'가 2번이상 연속된 부분은 하나로 치환
    wasDot = False
    str3 = ''
    for c in str2:
        if c != '.':
            wasDot = False
            str3 += c
        elif wasDot:
            continue
        elif c == '.':
            wasDot = True
            str3 += c
    print(str3)
    
    # 4. '.'가 양끝에 위치한다면 제거
    str3 = str3.strip('.')
    if str3 == '.':
        str3 == ''
    print(str3)
    
    # 5. 빈문자열이면 a를 대입
    if len(str3) == 0:
        str3 = 'a'
    print(str3)
    
    # 6. 16글자 이상이면, 앞쪽 15글자 외 제거, 끝에 위치한 마침표도 제거
    str3 = str3[:15]
    str3 = str3.strip('.')
    print(str3, len(str3))
    
    # 7. 길이 2이하면, 마지막 문자를 길이가 3이 될때까지 반복해서 붙인다
    while len(str3)<=2: 
        str3 += str3[-1]
    print(str3)    
    
    return str3
