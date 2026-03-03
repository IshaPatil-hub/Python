>>> f = open('chai.py')
>>> f.read
<built-in method read of _io.TextIOWrapper object at 0x00000278835EA880>
>>> f.readline()
'import time\n'
>>> f.readline()
'print("chai is here")\n'
>>> f.readline()
'username = "isha"\n'
>>> f.readline()
'print(username)'
>>> f.readline()
''
>>> f.readline()
''
>>> f.readline()
''

>>> f.__next__()
"# 'import time\\n'\n"
>>> f.__next__()
'# >>> f.readline()\n'
>>> f.__next__()
'# \'print("chai is here")\\n\'\n'
>>> f.__next__()
'# >>> f.readline()\n'
>>> f.__next__()
'# \'username = "isha"\\n\'\n'
>>> f.__next__()
'# >>> f.readline()\n'
>>> f.__next__()
"# 'print(username)'\n"
>>> f.__next__()
'# >>> f.readline()\n'
>>> f.__next__()
"# ''\n"
>>> f.__next__()
'# >>> f.readline()\n'
>>> f.__next__()
"# ''\n"
>>> f.__next__()
'# >>> f.readline()\n'
>>> f.__next__()
"# ''"
>>> f.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    f.__next__()
    ~~~~~~~~~~^^
StopIteration

>>> for line in open('chai.py'):
...     print(line)
... 
import time

print("chai is here")

username = "isha"

print(username)

>>> for line in open('chai.py'):
...     print(line, end='')     
... 
import time
print("chai is here")
username = "isha"
print(username)

>>> test = ""
>>> if not test:
...     print("chai")
... 
chai
>>> myList = [1, 2, 3, 4]
>>> I = iter(myList)
>>> I
<list_iterator object at 0x000002AF83B32830>
1
>>> I
<list_iterator object at 0x000002AF83B32830>
>>> I.__next__()
2
>>> I.__next__()
3
>>> I.__next__()
4
>>> I.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    I.__next__()
    ~~~~~~~~~~^^
StopIteration
>>> f = open('chai.py')
>>> iter(f) is f
True
>>> iter(f) is f.__iter__()
True
>>> myNewList = [1, 2, 3, 4]
>>> iter(myNewList) is myNewList
False
>>> D = {'a': 1, 'b':2} 
>>> for key in D.keys():
...     print(key)
... 
a
b
>>> I = iter(D)
>>> I
<dict_keyiterator object at 0x000001FBD1D0B0B0>
>>> next(I)
'a'
>>> next(I)
'b'
>>> next(I)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    next(I)
    ~~~~^^^
StopIteration
>>> range(5)
range(0, 5)
>>> R = range(5)
>>> I = iter(R)
>>> next(I)
0
>>> next(I)
1
>>> next(I)
2
>>> next(I)
3
>>> next(I)
4
>>> next(I)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    next(I)
    ~~~~^^^
StopIteration    