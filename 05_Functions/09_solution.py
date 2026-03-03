# Generate function with yeild
# Problem: Write a generator function that yields even numbers up to a specified limit.

# ___(return = Exit gate (no re-entry)
# yield = Pause button (resume later))
# Loop does not control function — return does
# For continuous output inside a loop → use yield___

def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i
    


for num in even_generator(10):
    print(num)              #Integer is NOT iterable



'''
def even_generator(limit):
    li = []
    for i in range(2, limit + 1, 2):
        li.append(i)
    return li

print(even_generator(10))    
    


>>> limit = 10
>>> for i in range(2, limit + 1, 2):
...     print(i)
... 
2
4
6
8
10
'''