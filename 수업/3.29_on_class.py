Python 3.10.4 (v3.10.4:9d38120e33, Mar 23 2022, 17:29:05) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
a_list = [ 1,2,3,4 ]
b_list = [ 5,6,7,8 ]
t_list = a_lsit + b_list
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    t_list = a_lsit + b_list
NameError: name 'a_lsit' is not defined. Did you mean: 'a_list'?
p
t_list = a_list + b_list
print(t_list)
[1, 2, 3, 4, 5, 6, 7, 8]
print(a_list*2)
[1, 2, 3, 4, 1, 2, 3, 4]
len(t_list)
8
print(len(a_lsit)/len(b_list))
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(len(a_lsit)/len(b_list))
NameError: name 'a_lsit' is not defined. Did you mean: 'a_list'?
print(len(a_list)/len(b_list))
1.0
print(len(a_list)/len(t_list))
0.5
a_list.clear()
print(a_list)
[]
b_list.count(7)
1
t_list.count(4)
1
b_list.index(6)
1
b_list.reverse()
b_list
[8, 7, 6, 5]
b_list.sort()
b_list
[5, 6, 7, 8]
10 in b_list
False
10 not in b_list
True
type(10 in b_list)
<class 'bool'>
sub_score = [ 78,95], [68,62]]
SyntaxError: unmatched ']'
sub_score = [ [78,95], [68,62]]
sub_score[0][1]
95
kor, eng = sub_score
type(kor)
<class 'list'>
print(kor)
[78, 95]
t_list = sub_score[0][0] + sub_score[0][1]
print(t_list)
173
t_kor = kor[0] + kor[1]
print(t_kor)
173
eng[0] = 86
print(eng)
[86, 62]
t_eng = eng[0]+eng[1]
print("국어점수 평균", t_kor,"점", "평균",t_kor/2)
국어점수 평균 173 점 평균 86.5
print("국어점수 총점 {}점, 평균 {}점".format(t_kor, t_kor/2))
국어점수 총점 173점, 평균 86.5점
print("영어점수 총점 {}점, 평균 {}점".format(t_eng, t_eng/2))
영어점수 총점 148점, 평균 74.0점
print("영어점수 총점 {}점, 평균 {}점".format(t_eng, t_eng/2))
영어점수 총점 148점, 평균 74.0점
print("영어점수 총점 {1}점, 평균 {1}점".format(t_eng, t_eng/2))
영어점수 총점 74.0점, 평균 74.0점







# 리스트 자료 수
data_list = [ 87, 95, 68, 92 ]
data_list*2
[87, 95, 68, 92, 87, 95, 68, 92]
score_list = [ data for data in data_list ]
score_list
[87, 95, 68, 92]
score_list = [ data*2 for data in data_list ]
score_list
[174, 190, 136, 184]
div_score = [ score for score in div_score ]
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    div_score = [ score for score in div_score ]
NameError: name 'div_score' is not defined. Did you mean: 'sub_score'?
div_score = [ score/3 for score in score_list ]
print(div_score)
[58.0, 63.333333333333336, 45.333333333333336, 61.333333333333336]
div_score = [ int(score/3) for score in score_list ]
print(div_score)
[58, 63, 45, 61]
adj_list = [ data + 5 for data in data_list ]
data_list
[87, 95, 68, 92]
adj_list
[92, 100, 73, 97]
scd_list = [ x-5 for x in data_list ]
scd_list
[82, 90, 63, 87]



# 자료의 구조: 사전
score
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    score
NameError: name 'score' is not defined


score = { "math":78, "englist":95,
          "science":68, "chemistry":62
          }
score
{'math': 78, 'englist': 95, 'science': 68, 'chemistry': 62}
score[0]
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    score[0]
KeyError: 0
score["math"]
78
type(score)
<class 'dict'>
score["music":86]
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    score["music":86]
TypeError: unhashable type: 'slice'
score["music"]=86
score
{'math': 78, 'englist': 95, 'science': 68, 'chemistry': 62, 'music': 86}
del score[0]
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    del score[0]
KeyError: 0
del score["math"]
score
{'englist': 95, 'science': 68, 'chemistry': 62, 'music': 86}


movie_dic = {
    "title" : "Avengers End Game"
    "type" : "Hero Movie"
    
SyntaxError: '{' was never closed
movie_dic = {
    "title" : "Avengers End Game"
    "type" : "Hero Movie"
    
SyntaxError: '{' was never closed
movie_dic = {
    "title" : "Avengers End Game"
    "type" : "Hero Movie"
    
SyntaxError: '{' was never closed
movie_dic = {
    "title" : "Avengers End Game"
    "type" : "Hero Movie"
    
SyntaxError: '{' was never closed
movie_dic = {
    "title" : "Avengers End Game",
    "type" : "Hero Movie",
    "director" : ["Ansony Luso","Joe Luso"],
    "cast" : ["Ironman","Tanos","Hulk","Doctor_stranger","Tor"],
    "theater" : ["CGV","Lotte_cinema"],
    "time" : [ 9,12,13,18,22 ]
    }
    
movie_dic["cast"][4]="Thor"
    
print("title: ", movie_dic["title"])
    
title:  Avengers End Game
print("cast: ", movie_dic["cast"])
    
cast:  ['Ironman', 'Tanos', 'Hulk', 'Doctor_stranger', 'Thor']
print("time: ", movie_dic["time"])
    
time:  [9, 12, 13, 18, 22]
movie_dic["price"]=12000
    
movie_dic
    
{'title': 'Avengers End Game', 'type': 'Hero Movie', 'director': ['Ansony Luso', 'Joe Luso'], 'cast': ['Ironman', 'Tanos', 'Hulk', 'Doctor_stranger', 'Thor'], 'theater': ['CGV', 'Lotte_cinema'], 'time': [9, 12, 13, 18, 22], 'price': 12000}
