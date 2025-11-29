def solution(genres, plays):

    # 가공
    songs = {}
    count = {}
    for i in range(len(genres)):
        if not songs.get(genres[i]):
            songs[genres[i]] = []
            count[genres[i]] = 0
        songs[genres[i]].append([plays[i], i])
        count[genres[i]] += plays[i]

    print(songs)
    print(count)

    for key, value in songs.items():
        songs[key] = sorted(value, key=lambda x: (-x[0], x[1]))
    count = sorted(count, reverse=True)

    print(songs) # {'classic': [[800, 3], [500, 0], [150, 2]], 'pop': [[2500, 4], [600, 1]]}
    print(count) # ['pop', 'classic']

    # 코드
    answer = []
    for genre in count:
        if len(songs[genre]) == 1:
            answer.append(songs[genre][0][1])
        else:
            answer.append(songs[genre][0][1])
            answer.append(songs[genre][1][1])

    print(answer)
    return answer

solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])