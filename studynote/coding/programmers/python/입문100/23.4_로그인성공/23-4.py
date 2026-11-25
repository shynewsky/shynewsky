def solution(id_pw, db):
    id_, pw_ = id_pw
    for i, p in db:
        if i == id_ and p == pw_:
            return 'login'
        elif i == id_ and p != pw_:
            return 'wrong pw'
    else:
        return 'fail'