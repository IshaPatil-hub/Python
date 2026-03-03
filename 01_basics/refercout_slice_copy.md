>>> import sys
>>> sys.getrefcount()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    sys.getrefcount()
    ~~~~~~~~~~~~~~~^^
TypeError: sys.getrefcount() takes exactly one argument (0 given)
>>> sys.getrefcount(24601)
3
>>> sys.getrefcount('hitesh')
3
>>> sys.getrefcount('h')         
4294967295
>>> sys.getrefcount('hitesh')
3
>>> sys.getrefcount('i')     
4294967295
>>> sys.getrefcount('isha')
3
>>> a = 3
>>> a = 'chaiaurcode'
>>> a = 3.14 
>>> a
3.14
>>> a = a + 2
>>> a
5.140000000000001
>>> myListOne = [1, 2, 3]
>>> mylisttwo = myListOne
>>> mylisttwo              
[1, 2, 3]
>>> myListOne = 'chai'   
>>> mylisttwo
[1, 2, 3]
>>> myListOne                  
'chai'
>>> myListOne = [1, 2, 3]
>>> myListOne            
[1, 2, 3]
>>> mylisttwo 
[1, 2, 3]
>>> myListOne[0] = 33
>>> myListOne        
[33, 2, 3]
>>> mylisttwo 
[1, 2, 3]
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> l2
[1, 2, 3]
>>> l1[0] = 44
>>> l1
[44, 2, 3]
>>> l2      
[44, 2, 3]
>>> l1 = "chai"
>>> l1
'chai'
>>> l2
[44, 2, 3]
>>> p1 = [1, 2, 3]
>>> p2 = p1
>>> p2 = [1, 2, 3]
>>> p1[0]=55   
>>> p1
[55, 2, 3]
>>> p2
[1, 2, 3]   