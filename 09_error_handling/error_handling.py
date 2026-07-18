
# x = ('Masala', 'lemon', 'ginger')
# y = enumerate(x)
# y
# # enumerate object at 0x000002AF29FD9D50
# list(y)
# [(0, 'Masala'), (1, 'lemon'), (2, 'ginger')]




file = open('youtube.txt', 'w')

try:
    file.write('chai aur code')
finally:
    file.close()
    
with open('youtube.txt', 'w') as file:
    file.write('chai aur python')