>>> x = 2
>>> y = 3
>>> z = 4
>>> x+y
5
>>> x**y
8
>>> z/x
2.0
>>> z//x
2
>>> z///x
  File "<stdin>", line 1
    z///x
       ^
SyntaxError: invalid syntax
>>> x + y * z
14
>>> (x + y) * z
20
>>> 40 + 2.23
42.23
>>> int(2.23)
2
>>> float(40)
40.0
>>> 'chai' + 'code'
'chaicode'
>>> 'chai' - 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    'chai' - 2
    ~~~~~~~^~~
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> 'chai' - 'chai'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    'chai' - 'chai'
    ~~~~~~~^~~~~~~~
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> x, y, z
(2, 3, 4)
>>> x + y, y*2
(5, 6)
>>> y % 2
1
>>> z ** 5  
1024
>>> 100  ** 2
10000
>>> 2 ** 1000
10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376
>>> result = 1/3.0
>>> result
0.3333333333333333
>>> repr('chai')
"'chai'"
>>> str('chai')
'chai'
>>> print('chai')
chai
>>> 1 < 2
True
>>> 1 > 2
False
>>> 5.0 == 5.0
True
>>> 4.0 != 5.0
True
>>> x, y, z
(2, 3, 4)
>>> x < y < z
True
>>> x < y and y < z 
True
>>> 1 == 2 < 3
False
>>> 1 == 2 and 2 < 3
False
>>> True == 2 and 2 < 3
False
>>> math. floor(3.5)
3
>>> math.floor(-3.5)
-4
>>> math.floor(3.9)
3
>>> math.trunc(2.8)
2
>>> math.trunc(-2.8)
-2
>>> 99999999999999999 + 1
100000000000000000
>>> 99999999999999999 * 2.1
2.1e+17
>>> 2 * 200
400
>>> 2**200
1606938044258990275541962092341162602522202993782792835301376
>>> (2 + 1j)
(2+1j)
>>> (2 + 1j) * 3
(6+3j)
>>> 0o20
16
octal literals are specified using a leading 0o (zero followed by the lowercase letter 'o') or 0O (zero followed by the uppercase letter 'O') prefix.
>>> 0xFF
255
>>> 0b1000
8
>>> oct(64)
'0o100'
hex(64)
'0x40'
>>> bin(64)
'0b1000000'
>>> int(3.14)
3
>>> int(64)
64
>>> int('64', 8)
52
>>> int('10000', 2)
16
>>> x = 1
>>> x 
1
>>> x << 2
4
>>> x | 2
3
>>> import random
>>> random.random()
0.7314490038953921
>>> random.randint(1, 10)  
10
>>> random.randint(1, 10)
8
>>> random.randint(1, 10)
9
>>> random.randint(1, 10)
6
>>> random.choice(l1)
'mint'
>>> random.choice(l1)
'masala'
>>> random.choice(l1)
'lemon'
>>> random.shuffle(l1)
>>> l1
['ginger', 'lemon', 'mint', 'masala']
>>> 0.1
0.1
>>> 0.1 + 0.1
0.2
>>> 0.1 + 0.1 + 0.4
0.6000000000000001
>>> 0.1 + 0.1 + 0.1
0.30000000000000004
>>> 0.1 + 0.1 + 0.1 - 0.3
5.551115123125783e-17
>>> (0.1 + 0.1 + 0.1) - 0.3
5.551115123125783e-17
>>> from decimal import Decimal
>>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1')
Decimal('0.3')
>>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
Decimal('0.0')                       #-to learn more about the these numbers decimal context manager
>>> from fractions import Fraction
>>> myFra
>>> myFra = Fraction(2,7)
>>> myFra
Fraction(2, 7)
>>> setone = {1, 2, 3, 4}
>>> setone                 
{1, 2, 3, 4}
>>> setone & {1, 3}
{1, 3}
>>> setone | {1, 3}    
{1, 2, 3, 4}
>>> setone | {1, 3, 7}
{1, 2, 3, 4, 7}
>>> setone            
{1, 2, 3, 4}
>>> setone - {1, 2, 3, 4}
set()
>>> type({})
<class 'dict'>
>>> type(True)
<class 'bool'>
>>> True == 1
True
>>> False == 0
True
>>> True is 1
<stdin-127>:1: SyntaxWarning: "is" with 'int' literal. Did you mean "=="?
False
>>> True + 4
5