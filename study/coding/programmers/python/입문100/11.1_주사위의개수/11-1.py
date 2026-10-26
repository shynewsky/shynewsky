def solution(box, n):
    width = box[0] // n
    depth = box[1] // n
    height = box[2] // n
    return width * depth * height
