def solution(quiz):
    answer = []
    for equation in quiz:
        a, op, b, eq, c = equation.split()
        if op == '+' and int(a) + int(b) == int(c):
            answer.append("O")
        elif op == '-' and int(a) - int(b) == int(c):
            answer.append("O")
        else:
            answer.append("X")

    return answer
