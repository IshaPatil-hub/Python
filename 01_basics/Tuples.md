>>> tea_types = ("Black", "Green", "Oolong")
>>> tea_types
('Black', 'Green', 'Oolong')
>>> tea_types[0]
'Black'
>>> tea_types[-1]
'Oolong'
>>> tea_types[1:]
('Green', 'Oolong')
>>> tea_types[0] = "Lemon"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    tea_types[0] = "Lemon"
    ~~~~~~~~~^^^
TypeError: 'tuple' object does not support item assignment
>>> len(tea_types)
3
>>> more_tea = ("Herbal", "Earl Grey")
>>> all_tea = more_tea + tea_types
>>> all_tea
('Herbal', 'Earl Grey', 'Black', 'Green', 'Oolong')
>>> if "Green" in all_tea:
...     print("I have green tea")
... 
I have green tea
>>> more_tea.count("Herbal")
1
>>> tea_types
('Black', 'Green', 'Oolong')
>>> (black, green, Oolong) = tea_types
>>> black
'Black'
>>> type(tea_types)
<class 'tuple'>
