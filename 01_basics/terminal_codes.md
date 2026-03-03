>>> 77*88
6776
>>> "chai"*5 
'chaichaichaichaichai'
>>> score=100
>>> score
100
>>> import os
>>> os.getcwd()
'C:\\Users\\Admin\\programs for practice\\chaiaurpython'
>>> for c in "chai":
...     print(c)    
... 
c
h
a
i
>>>>>> import sys
>>> sys.platform
'win32'
>>> import Hello_python
Hello World
chai aur code
green tea
>>> Hello_python.chai("mint tea")
mint tea
>>> Hello_python.chai_one
'lemon tea'
>>> from importlib import reload
>>> reload(Hello_python)
Hello World
chai aur code
green tea
<module 'Hello_python' from 'C:\\Users\\Admin\\programs for practice\\chaiaurpython\\Hello_python.py'>
>>> username="Isha"
>>> username
'Isha'
>>> username="chaiaurcode"
>>> username
'chaiaurcode'
>>> x=10
>>> y=x
>>> y
10
>>> x
10
>>> mylist=[1,2,3,['a','b']]
>>> mylist
[1, 2, 3, ['a', 'b']]
>>> 12*12
144
>>> import math
>>> math.pi
3.141592653589793
>>> import random
>>> random.random()
0.04286892457448821
>>> random.choice([1,2,3,4])
1
>>> random.choice
<bound method Random.choice of <random.Random object at 0x000001ED0D165EC0>>
>>> len("username")
8
>>> username[0]
'c'
>>> username[0]="A"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    username[0]="A"
    ~~~~~~~~^^^
TypeError: 'str' object does not support item assignment
>>> username[-1] 
'e'
>>> username[-2]
'd'
>>> username[1:3]
'ha'
>>> dir(username)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> mylist={123,"chai",3.14}
>>> mylist
{3.14, 'chai', 123}
>>> len(mylist)
3
>>> mylist[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    mylist[0]
    ~~~~~~^^^
TypeError: 'set' object is not subscriptable
>>> mylist[-1]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    mylist[-1]
    ~~~~~~^^^^
TypeError: 'set' object is not subscriptable
>>> myD={'one':'lemon, 'two':'ginger', 'three':'nagraj'}
  File "<stdin>", line 1
    myD={'one':'lemon, 'two':'ginger', 'three':'nagraj'}
               ^^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> myD={'one':'lemon', 'two':'ginger', 'three':'nagraj'}
>>> myD
{'one': 'lemon', 'two': 'ginger', 'three': 'nagraj'}
>>> myTup={1,2,3,4}
>>> myTup[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    myTup[0]
    ~~~~~^^^
TypeError: 'set' object is not subscriptable
>>> len(myTup)
4

#SLICING
>>> h1 = [1, 2, 3] 
>>> h2 = h1[:]
>>> h1
[1, 2, 3]
>>> h2
[1, 2, 3]
>>> h1
[1, 2, 3]
>>> h1[0] = 55
>>> h1
[55, 2, 3]
>>> h2
[1, 2, 3]
>>> import copy
>>> h2 = copy.copy(h1)
>>> h2 = copy.deepcopy(h1)
>>> n = [1, 2, 3]
>>> m = n
>>> m
[1, 2, 3]
>>> m == n
True
>>> m is n
True
>>> m = [1, 2, 3]
>>> m is n
False