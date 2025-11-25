def solution(genres, plays):

    # 가공
    n = len(genres)
    select_song = {}  # ['pop', 'classic']
    select_genre = {} # {'classic': [[500, 0], [150, 2], [800, 3]], 'pop': [[600, 1], [2500, 4]]}

    for i in range(n):
        if select_song.get(genres[i]):
            select_song[genres[i]].append([plays[i], i])
            select_genre[genres[i]] += plays[i]
        else:
            select_song[genres[i]] = [[plays[i], i]]
            select_genre[genres[i]] = plays[i]

    for key, value in select_song.items():
        select_song[key] = sorted(value, key=lambda x: (-x[0], x[1]))
    select_genre = sorted(select_genre, reverse=True)

    # 코드
    answer = []
    for genre in select_genre:
        answer.append(select_song[genre][0][1])
        answer.append(select_song[genre][1][1])

    print(answer)
    return answer

solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])