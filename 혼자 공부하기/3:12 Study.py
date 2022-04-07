Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
ㅁ = "pithon"
a[:1]
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a[:1]
NameError: name 'a' is not defined
a = "pithon"
a[:1]
'p'
a = "ithon"
a = "Pithon"
a[:1]
'P'
a[2:]
'thon'
a[:1] + 'y' + a[2:]
'Python'
"I eat %d apples." %3
'I eat 3 apples.'
"I eat %s apples." % "five"
'I eat five apples.'
number = 3
"I eat %d apples." %number
'I eat 3 apples.'
number = 10
day = "three"
"I ate %d apples. so I was sick for %s days." %(number, day)
'I ate 10 apples. so I was sick for three days.'
"I ate %s apples." $3
SyntaxError: invalid syntax
"I ate %s apples." %3
'I ate 3 apples.'
"rate is %s" %3.234
'rate is 3.234'
"Error is %d%." % 98
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    "Error is %d%." % 98
ValueError: incomplete format
"Error is %d%%." % 98
'Error is 98%.'
print(a)