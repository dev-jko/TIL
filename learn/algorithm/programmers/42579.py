def solution(genres, plays):
    genres_dic = {}
    for i in range(len(genres)):
        m = Music(i, genres[i], plays[i])
        if genres[i] in genres_dic:
            dic = genres_dic[genres[i]]
            dic[0] += m.plays
            dic[1].append(m)
        else:
            genres_dic[genres[i]] = [m.plays, [m]]

    genres = sorted(list(set(genres)), key=lambda x: genres_dic[x][0], reverse=True)
    answer = []

    for g in genres:
        genres_dic[g][1].sort(key=lambda x: x.plays, reverse=True)
        for music in genres_dic[g][1][:2]:
            answer.append(music.id)
    return answer

class Music:
    def __init__(self, id, genre, plays):
        self.id = id
        self.genre = genre
        self.plays = plays
        
    