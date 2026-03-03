>>> chai = "Lemom Chai"
>>> chai
'Lemom Chai'
>>> print(chai)
Lemom Chai
>>> chai = "Masala Chai"
>>> first_char = chai[0]
>>> print(first_char)
M
>>> chai
'Masala Chai'
>>> slice_chai = chai[0:6]
>>> print(slice_chai)
Masala
>>> chai[0:6]
'Masala'
>>> chai[-1]
'i'
>>> num_list = "0123456789"
>>> num_list[:]
'0123456789'
>>> num_list[3:]
'3456789'
>>> num_list[:7]
'0123456'
>>> num_list[0:7:2]             #Hopping value
'0246'
>>> num_list[0:7:3]
'036'
>>> print(chai.upper())
MASALA CHAI
>>> chai
'Masala Chai'
>>> chai = "    Masala   chai   "
>>> chai
'    Masala   chai   '
>>> print(chai.strip())
Masala   chai
>>> chai
chai = "lemon chai"
>>> print(chai)
lemon chai
>>> chai = "Lemon, Ginger, Masala, Mint"
>>> chai
'Lemon, Ginger, Masala, Mint'
>>> print(chai.split())
['Lemon,', 'Ginger,', 'Masala,', 'Mint']
>>> print(chai.split(", "))
['Lemon', 'Ginger', 'Masala', 'Mint']
chai = "Masala chai"    
>>> print(chai.find("chai"))
7
>>> print(chai.find("Chai"))
-1                     #if we did not find anything then it returns -1
>>> print(chai.count("Chai"))
3
>>> print(chai.count("Chai"))
3
>>> chai_type = "Masala"
>>> quantity = 2
>>> order = "I ordered {} cups of {} chai"
>>> order
'I ordered {} cups of {} chai'
>>> print(order.format(quantity, chai_type))
I ordered 2 cups of Masala chai
>>> chai_variety = ["Lemon", "Masala", "Ginger"]
>>> chai_variety
['Lemon', 'Masala', 'Ginger']
>>> print("".join(chai_variety))
LemonMasalaGinger
>>> print("  ".join(chai_variety))
Lemon  Masala  Ginger
>>> print("- ".join(chai_variety))
Lemon- Masala- Ginger
>>> print(",  ".join(chai_variety))
Lemon,  Masala,  Ginger
>>> chai = "Masala chai"
>>> chai
'Masala chai'
>>> print(len(Masala))
>>> print(len(chai))                            
11
>>> for letter in chai:
...     print(letter)
... 
M
a
s
a
l
a

c
h
a
i
>>> chai = "He said, \"Masala chai is awesome\" "
>>> chai
'He said, "Masala chai is awesome" '
>>> chai = "Masala\nChai"
>>> chai
'Masala\nChai'
>>> print(chai)
Masala
Chai
>>> chai = r"Masala\nchai"     #r-prints raw value 
>>> print(chai)
Masala\nchai    #raw value
>>> chai = r"c:\\user\chai\nchai"
>>> print(chai)
c:\\user\chai\nchai
>>> chai
'c:\\\\user\\chai\\nchai'
>>> chai = r"c:\\user\\chaiaurpython\\"
>>> print(chai)
c:\\user\\chaiaurpython\\
>>> print(chai)
c:\\user\\chaiaurpython\\
>>> chai = r"c:\user\pwd"
>>> chai   
'c:\\user\\pwd'
>>> print(chai)
c:\user\pwd
>>> chai = "Masala Chai"
>>> print("Masala" in chai)
True
>>> print("Masalaa" in chai)
False