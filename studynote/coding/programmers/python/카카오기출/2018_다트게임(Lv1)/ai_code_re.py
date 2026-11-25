import re

def solution(dartResult: str) -> int:
    tokens = re.findall(r'(\d+)([SDT])([*#]?)', dartResult)
    pts = []
    powmap = {'S':1, 'D':2, 'T':3}
    
    for a, b, c in tokens:
        x = int(a) ** powmap[b]
        if c == '*':
            if pts:
                pts[-1] *= 2
            x *= 2
        elif c == '#':
            x *= -1
        pts.append(x)
        
    return sum(pts)
