movie_dic = {
    "title": "Avengers End Game",
    "type": "Hero Movie",
    "director": ["Ansony Luso","Joe Luso"],
    "cast": ["Ironman","Tanos","Hulk","Doctor_strange","Thor"],
    "theater": ["CGV","Lotte_cinema"],
    "time": [ 9,12,13,18,22 ]
    }

print(type(movie_dic["time"]))
del movie_dic["cast"][1]
print(movie_dic["theater"][1])
movie_dic["evaluate"]="*"*10
movie_dic["time"] = [ t-1 for t in movie_dic["time"] ]
print("title:", movie_dic["title"])
print("cast:", movie_dic["cast"])
print("time:", movie_dic["time"])
print("evaluate:", movie_dic["evaluate"])
