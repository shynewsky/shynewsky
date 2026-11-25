def solution(phone_book):
    n = len(phone_book)
    no_prefix = True
    for i in range(n):
        m = len(phone_book[i])
        for phone in phone_book[:i]:
            if phone_book[i] == phone[:m]:
                no_prefix = False
        for phone in phone_book[i+1:]:
            if phone_book[i] == phone[:m]:
                no_prefix = False
    return no_prefix

solution(["119", "97674223", "1195524421"])
solution(["123","456","789"])
solution(["12","123","1235","567","88"])