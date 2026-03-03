# Function with *args
# Problem: Write a function that takes number of arguments and returns their sum.

def sum_all(*args):
    print(*args)
    
    for i in args:          #Important Python rule to remember   
                            #In Python, loop variables (i, x, item) are implicitly created by the for loop and assigned values during iteration.
       print(i * 2)
    return sum(args)

print(sum_all(1, 2, 3))
print(sum_all(1, 2, 3, 4, 5))
print(sum_all(1, 2, 3, 4, 5, 6, 7, 8))