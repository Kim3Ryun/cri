Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
t_tuple = ( a,b,c,d,e )
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    t_tuple = ( a,b,c,d,e )
NameError: name 'a' is not defined
t_tuple = ( 'a', 'b', 'c', 'd', 'e' )
t_tuple[2]
'c'
t_tuple[2:]
('c', 'd', 'e')
t_tuple[-2:]
('d', 'e')
t_tuple[-2]
'd'
t_list = [ 76, 86. 87, 93 ]
SyntaxError: invalid syntax. Perhaps you forgot a comma?
t_list = [ 76, 86, 87, 93 ]
print(t_list)
[76, 86, 87, 93]
t_list[3]
93
t_list[0]
76
t_list[2:]
[87, 93]
t_list[:-2]
[76, 86]
t_list.append(90)
print(t_list)
[76, 86, 87, 93, 90]
t_list.insert(2,93)
print(t_list)
[76, 86, 93, 87, 93, 90]
t_list.remove(86)
print(t_list)
[76, 93, 87, 93, 90]
remove.t_list(90)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    remove.t_list(90)
NameError: name 'remove' is not defined
t_list.pop(0)
76
remove.t_list(90)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    remove.t_list(90)
NameError: name 'remove' is not defined
print(t_list)
[93, 87, 93, 90]
del t_list[2]
print(t_list)
[93, 87, 90]
t_list.indexing(100)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    t_list.indexing(100)
AttributeError: 'list' object has no attribute 'indexing'
t_list.indexing[100]
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    t_list.indexing[100]
AttributeError: 'list' object has no attribute 'indexing'
AttributeError: 'list' object has no attribute 'indexing'
SyntaxError: invalid syntax
print(t_list)
[93, 87, 90]
t_list.attend(100)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    t_list.attend(100)
AttributeError: 'list' object has no attribute 'attend'. Did you mean: 'append'?
t_list.append(100)
t_list.insert(3,89)
del t_list(87)
SyntaxError: cannot delete function call
del t_list[87]
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    del t_list[87]
IndexError: list assignment index out of range
print(t_list)
[93, 87, 90, 89, 100]
del t_list[2]
print(t_list)
[93, 87, 89, 100]
t_list.insert(2,90)
del t_list[1]
print(t_list)
[93, 90, 89, 100]
t_list[0] + t_list[1] +t_list[2] + t_list[3]
372
total : t_list[0] + t_list[1] +t_list[2] + t_list[3]
print(total)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    print(total)
NameError: name 'total' is not defined
total = t_list[0] + t_list[1] +t_list[2] + t_list[3]
print(total)
372
t_list = [ [93,90],[89,100] ]
t_list[0]
[93, 90]
t_list[0][0]
93
t_list[1][1]
100
kor_t = t_list[0][0]+t_list[0][1]
print(kor_t)
183
eng_t = t_list[1][0]+t_list[1][1]
eng_a = eng_t/2
print(eng_t)
189
print(eng_a)
94.5
print(eng_t, eng_t/2)
189 94.5
kor, eng = t_list
kor
[93, 90]
eng
[89, 100]
type(eng)
<class 'list'>
t_kor = kor[0]+kor[1]
print(t_kor)
183
del t_list[1][0]
print(eng)
[100]





print("AIstudy\n"*3)
AIstudy
AIstudy
AIstudy

print(type(true))
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    print(type(true))
NameError: name 'true' is not defined. Did you mean: 'True'?
print(type(3.17), type(true))
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    print(type(3.17), type(true))
NameError: name 'true' is not defined. Did you mean: 'True'?
type(3.17), type(22)
(<class 'float'>, <class 'int'>)
type(true)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    type(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
print(true)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    print(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
type(True)
<class 'bool'>
type(False)
<class 'bool'>
type("AI")
<class 'str'>










= RESTART: /Users/kimseryun/Documents/python on classs/수업/3.24 Quiz.김세륜.py

*************************
2분반	12345학번	성명: 한림대
*************************

# 원뿔의 겉넓이와 부피
반지름? 12
높이? 20
부채꼴의 반지름? 15
원뿔의 겉넓이:  1017.9
원뿔의 부피:  9047.8
