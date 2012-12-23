# Reverse a list


list = [0, 1, 2, 3, 4, 5]

# Using the reverse function - modifies the list in place

def reverse1(list):
    list.reverse()
    return list

# Or, using extended slice syntax - makes a shallow copy of the list

def reverse2(list):
    return list[::-1]

# Reverse2 keeps returning the same result because the list being
# passed is not itself being changed when the function runs. So, you
# get the same result because you are seeing the shallow copy created
# by the slicing operation and not a modified version of the original
# list. Viz:

ls = ['a', 'b', 'c']

reverse1(ls)
print(ls)  # ['c', 'b', 'a'] - modified in place
reverse1(ls)
print(ls)  # back to original

reverse2(ls) # ['c', 'b', 'a'] - shallow copy
print(ls)    # ['a', 'b', 'c'] - original unmodified
