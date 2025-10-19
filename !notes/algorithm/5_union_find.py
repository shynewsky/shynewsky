'''
# parents[]
idx(c)  1   2   3   4   5   6
ele(p)  1   2   3   4   5   6
set     {1} {2} {3} {4} {5} {6}

# ranks[]
idx(c)  1   2   3   4   5   6
ele(s)  0   0   0   0   0   0
'''
'''
union(2,4) 했을때

# parents[]
idx(c)  1   2     3   4   5   6
ele(p)  1   2     3   2   5   6
set     {1} {2,4} {3} {}  {5} {6}

# ranks[]
idx(c)  1   2   3   4   5   6
ele(s)  0   1   0   0   0   0
'''

# ---------------------------------------------------------------------

def make_set1(V):
    parents = [i for i in range(V+1)]
    return parents

# 우선순위 : 서브트리의 높이를 Rank로 저장하여, 작은 트리를 큰 트리에 붙인다
def make_set2(V):
    parents = [i for i in range(V+1)]
    ranks = [0] * (V+1)   # 여기
    return parents, ranks # 여기

# ---------------------------------------------------------------------

def find_set1(x):
    if x == parents[x]: # 자식이 부모와 같으면 대표자
        return x
    return find_set1(parents[x]) # 부모의 부모를 다시 검색

# 경로압축 : 후손들의 부모를 통일하여, 검색 속도를 단축한다
def find_set2(x):
    if x == parents[x]:
        return x
    parents[x] = find_set2(parents[x]) # 여기
    return parents[x]                  # 여기

# ---------------------------------------------------------------------



def union1(x, y):
    rep_x = find_set1(x) # 대표자 검색
    rep_y = find_set1(y)
    if rep_x == rep_y:  # 대표자가 같으면 같은 집합 => 합치지 않음
        return

    parents[rep_x] = rep_y

# 대표자 값이 작은쪽으로 연결하기
def union2(x, y):
    rep_x = find_set2(x)
    rep_y = find_set2(y)
    if rep_x == rep_y:
        return

    if rep_x < rep_y:           # 여기
        parents[rep_y] = rep_x  # 여기
    else:                       # 여기
        parents[rep_x] = rep_y  # 여기

# 트리가 큰 쪽으로 연결하기
def union3(x, y):
    rep_x = find_set2(x)
    rep_y = find_set2(y)
    if rep_x == rep_y:
        return

    if ranks[rep_x] < ranks[rep_y]:
        parents[rep_x] = rep_y
    elif ranks[rep_y] < ranks[rep_x]:
        parents[rep_y] = rep_x
    else:                       # 트리 깊이가 동일할때는
        parents[rep_y] = rep_x  # 한쪽으로 병합하고
        ranks[rep_x] += 1       # 트리 깊이를 +1 한다

# ---------------------------------------------------------------------

parents, ranks = make_set2(6)
union3(2, 4)