# Find the second to last box of a list.


list = [0, 1, 2, 3, 4, 5]

list[-2] # Negative indexing

list[len(list)-2] # Explicit

# As a function

def penultimate(list):
    return list[-2]
