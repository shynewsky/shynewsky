import re

def solution(new_id):

    new_id = new_id.lower()
    
    new_id = re.sub(r'[^a-z0-9\-\._]', '', new_id)
    	# 정규식: a-z, 0-9, -, _, . 가 아닌 모든 문자    
        
    new_id = re.sub(r'\.+', '.', new_id)
    	# 정규식: \.+ -> 마침표가 1개 이상 연속된 패턴
        
    new_id = new_id.strip('.')
    
    if not new_id:
        new_id = 'a'
        
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = new_id.strip('.')
        
    while len(new_id) <= 2:
        new_id += new_id[-1]        
        
    return new_id
