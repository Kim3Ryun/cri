Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
print(123)
123

= RESTART: /Users/kimseryun/Documents/python on classs/수업/3:15 class.py
#파이썬 사칙연산
7+4= 11
7-4= 3
7*4= 28
7/4= 1.75

7//4= 1
7%4= 3
7**4= 2401

파이썬
사칙연산
파이썬	사칙연산
파이썬 사칙연산파이썬 사칙연산
type("python")
<class 'str'>
type(12345)
<class 'int'>
type(123,45)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    type(123,45)
TypeError: type() takes 1 or 3 arguments
type(123.45)
<class 'float'>
type(true)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    type(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
type(True)
<class 'bool'>
type(12345)
<class 'int'>
type("인공지능")
<class 'str'>
type(123.45)
<class 'float'>
type(True)
<class 'bool'>
print("AI인공지능")
AI인공지능
print(""AI인공지능"")
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print('"AI인공지능"')
"AI인공지능"
print("\"AI인공지능\"")
"AI인공지능"
print("\"AI인공\n지능\"")
"AI인공
지능"
print("AI인공\n지능")
AI인공
지능
print("AI인공\t지능")
AI인공	지능
print("""
AI인공지능 융합학부""")

AI인공지능 융합학부
print("""
AI인공지능 융합학부
""")

AI인공지능 융합학부

print("""\
AI인공지능 융합학부\
""")
AI인공지능 융합학부
print('''\
AI인공지능 융합학부\
''')
AI인공지능 융합학부
print('''\
AI인공지능\n융합학부\
''')
AI인공지능
융합학부
print("AI"+"인공지능"+"융합")
AI인공지능융합
print("AI"+"인공지능"-"융합")
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print("AI"+"인공지능"-"융합")
TypeError: unsupported operand type(s) for -: 'str' and 'str'
print("AI"*2,"인공지능"*3)
AIAI 인공지능인공지능인공지능
print("AI"*2,"인공지능"*3)
AIAI 인공지능인공지능인공지능
print("AI인공지능\n"*10)
AI인공지능
AI인공지능
AI인공지능
AI인공지능
AI인공지능
AI인공지능
AI인공지능
AI인공지능
AI인공지능
AI인공지능

print("AI인공지능\t"*10)
AI인공지능	AI인공지능	AI인공지능	AI인공지능	AI인공지능	AI인공지능	AI인공지능	AI인공지능	AI인공지능	AI인공지능	
print("AI인공지능\t"[0])
A
print("AI인공지능\t"[1])
I
print("AI인공지능\t"[2])
인
print("AI인공지능\t"[3])
공
print("AI인공지능\t"[4])
지
print("AI인공지능\t"[0:3])
AI인
print("AI인공지능\t"[2:3])
인
print("AI인공지능\t"[2:4])
인공
print("AI인공지능\t"[2:5])
인공지
print("AI인공지능\t"[2:6])
인공지능
print("AI인공지능\t"[2:])
인공지능	
print("AI인공지능\t"[4:])
지능	
print("AI인공지능\t"[:3])
AI인
print("AI인공지능\t"[-2:-6])

print("AI인공지능\t"[-6:-2])
I인공지
print("AI인공지능\t"[-5:-2])
인공지
print("AI인공지능"[-5:-2])
I인공
print("AI인공지능"[:-3])
AI인
len("인공지능융합학부")
8
type(len("인공지능"))
<class 'int'>
print(len("인공지능")+len("융합학부"))
8
type(123.45)
<class 'float'>
int(123.45)
123
float(123)
123.0
int(True)
1
int(False)
0
float(True)
1.0
str(123)
'123'
type(str(123))
<class 'str'>
str(-12345)
'-12345'
type(True)
<class 'bool'>
bool(123)
True
bool(0)
False
bool(-123)
True
bool(123.45)
True
bool(0.0))
SyntaxError: unmatched ')'
bool(0.0)
False
bool(tree)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    bool(tree)
NameError: name 'tree' is not defined. Did you mean: 'True'?
bool("tree")
True
bool("Tree")
True
bool(" ")
True
bool("")
False
