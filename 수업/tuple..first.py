Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
total = 100
total = total + 50
total
150
total +=50
total
200
total *=2
total
400
total /+4
100.0
totae *=4
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    totae *=4
NameError: name 'totae' is not defined. Did you mean: 'total'?
total *=4
total
1600
total /=16
total
100.0

subject_score = (78,95,68,62)
type(subject_score)
<class 'tuple'>
subject_score = [ 78,95,68,62 ]
type(subject_score)
<class 'list'>
subject_score = {
    "kor":78,"eng":95,"math",68,"che":62 }
SyntaxError: ':' expected after dictionary key
subject_score = {
    "kor":78,"eng":95,"math":68,"che":62 }
type(subject_score)
<class 'dict'>


subject_score = ( 78,95,68,62 )

subject_score
(78, 95, 68, 62)
subject_score[0]
78
subject_score[4]
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    subject_score[4]
IndexError: tuple index out of range
subject_score[3]
62
subject_score[1:3]
(95, 68)
subject_score[1:]
(95, 68, 62)
subject_score[:2]
(78, 95)
total = subject
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    total = subject
NameError: name 'subject' is not defined. Did you mean: 'object'?
total = subject_score[0:4]
total
(78, 95, 68, 62)
total = subject_score[0]+subject_score[2]+subject_score[3]+subject_score[1]
total
303
avr = total / 4
avr
75.75
print("과목 총점:",total,"과목평균:",avr)
과목 총점: 303 과목평균: 75.75




subject_score = (78,95,68,62)


kor,eng,math,che=subject_score
kor
78
eng
95
math
68
che
62
total = kor + eng
total = kor + eng + math + che
total
303
avr = total / 4
avr
75.75



subject_score = ( (78,95),(68,62) )


subject_score[0]
(78, 95)
subject_score[0][0]
78
subject_score[0][1]
95
subject_score[1][0]
68
subject_score[1][1]
62
kor_t = subject_score[0][0] + subject_score[0][1]
kor_t
173


subject_score = ( (78,95),(68,62) )

kor, eng = subject_score
kor
(78, 95)
eng
(68, 62)
kor_t = kor[0]+kor[1]
kor_t
173
eng_t = eng[0]+eng[1]
eng_t
130
