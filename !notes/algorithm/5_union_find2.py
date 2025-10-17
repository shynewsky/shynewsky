# -------------------------------------------

'''
members  1   2   3   4   5   6
parents  1   2   3   4   5   6
set     {1} {2} {3} {4} {5} {6}
'''

def make_set(n):
    parents = [i for i in range(n+1)]
    return parents

# -------------------------------------------

'''
members  1   2   3   4   5   6
parents  1   2   3   4   5   6
set     {1} {2} {3} {4} {5} {6}
'''

def find_set(x):
    if x == parents[x]: # 자식이 부모와 같으면 대표자
        return x
    return find_set(parents[x]) # 부모의 부모를 다시 검색

# -------------------------------------------

'''
# union(2,4)
members  1   2     3   4   5   6
parents  1   2     3   2   5   6
set     {1} {2,4} {3} {}  {5} {6}

# union(4,6)
members  1   2       3   4   5   6
parents  1   2       3   2   5   2
set     {1} {2,4,6} {3}  {}  {5} {}
'''

'''
a → b → c → d → e → f
p[e] = f
p[d] = f
p[c] = f
p[b] = f
p[a] = f
'''
'''


'''


def union(x, y):
    rep_x = find_set(x) # 대표자 검색
    rep_y = find_set(y)

    if rep_x == rep_y: # 대표자가 같으면 같은 집합 => 합치지 않음
        return

    if rep_x < rep_y: # 대표자를 바꾼다
        parents[rep_y] = rep_x
    else:
        parents[rep_x] = rep_y

# -------------------------------------------

N = 6
parents = make_set(N)
union(2, 4)
union(4, 6)

if find_set(2) == find_set(6): # 대표자 같으면 같은 집합
    print('같은 집합')
else:                          # 대표자 다르면 다른 집합
    print('다른 집합')
