>>> tea_varities = ["Black", "Green", "Oolong", "White"]
>>> tea_varities
['Black', 'Green', 'Oolong', 'White']
>>> print(tea_varities)
['Black', 'Green', 'Oolong', 'White']
>>> print(tea_varities[0])
Black
>>> print(tea_varities[-1])
White
>>> print(tea_varities[1:3])
['Green', 'Oolong']
>>> print(tea_varities[:2]) 
['Black', 'Green']
>>> print(tea_varities[2:])
['Oolong', 'White']
>>> print(tea_varities[0:3:1])
['Black', 'Green', 'Oolong']
>>> print(tea_varities[0:4:2]) #Hopping value
['Black', 'Oolong']
>>> tea_varities[3] = "Herbal"
>>> print(tea_varities)
['Black', 'Green', 'Oolong', 'Herbal']
>>> tea_varities[1:2]
['Green']
>>> tea_varities[1] = "Lemon"
>>> tea_varities             
['Black', 'Lemon', 'Oolong', 'Herbal']
>>> tea_varities[1:2] = "Lemon"
>>> tea_varities
['Black', 'L', 'e', 'm', 'o', 'n', 'Oolong', 'Herbal']
>>> tea_varities = ["Black", "Green", "Oolong", "White"]
>>> tea_varities[1:2]
['Green']
>>> tea_varities[1:2] = ["Lemon"]
>>> tea_varities     
['Black', 'Lemon', 'Oolong', 'White']
>>> tea_varities[1:3]
['Lemon', 'Oolong']
>>> tea_varities[1:3] = ["green", "Masala"]
>>> tea_varities[1:3]                      
['green', 'Masala']
>>> tea_varities      
['Black', 'green', 'Masala', 'White']
>>> tea_varities
['Black', 'green', 'Masala', 'White']
>>> tea_varities[1:1]
[]
>>> tea_varities[1:1] = ["test", "test"]
>>> tea_varities
['Black', 'test', 'test', 'green', 'Masala', 'White']
>>> tea_varities[1:3] = []
>>> tea_varities
['Black', 'green', 'Masala', 'White']
>>> for tea in tea_varities:
...     print(tea)
... 
Black
green
Masala
White
...     print(tea, end="-") 
... 
Black-green-Masala-White->>> 
>>> tea_varities
['Black', 'green', 'Masala', 'White']
>>> if "Oolong" in tea_varities:
...     print("I have Oolong tea")
... 
>>> tea_varities.append("Oolong")
>>> tea_varities                 
['Black', 'green', 'Masala', 'White', 'Oolong']
>>> if "Oolong" in tea_varities: 
...     print("I have Oolong Tea")
... 
I have Oolong Tea
>>> tea_varities.pop()
'Oolong'
>>> tea_varities                  
['Black', 'green', 'Masala', 'White']
>>> tea_varities.remove("green") 
>>> tea_varities
['Black', 'Masala', 'White']
>>> squared_nums = [x**2 for x in range(10)]
>>> range(0, 10)
range(0, 10)
>>> print(range(10))
range(0, 10)
>>> y = range(10)
>>> y
range(0, 10)
squared_nums = [x**2 for x in range(10)]
>>> squared_nums                             
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> cube_num = [y**3 for y in range(5)]
>>> cube_num                           
[0, 1, 8, 27, 64]