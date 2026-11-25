dict = {
    "up":[0,1],
    "down":[0,-1],
    "left":[-1,0],
    "right":[1,0],
}

def solution(keyinput, board):
    x, y = 0, 0
    w, h = board
    for dir in keyinput:
        dx, dy = dict[dir]
        nx, ny = x + dx, y + dy
        if -(w//2)<=nx<=(w//2) and -(h//2)<=ny<=(h//2):
            x, y = nx, ny
        else:
            if nx < -(w//2):
                x = -(w//2)
            elif nx > w//2:
                x = w//2
            if ny < -(h//2):
                y = -(h//2)
            elif ny > h//2:
                y = h//2

    return [x, y]
