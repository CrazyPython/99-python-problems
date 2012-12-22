# Reverse a list


list = [0, 1, 2, 3, 4, 5]

# Reverse a list - modifies the list in place

def reverse1(list):
    list.reverse()
    return list

# Or, using extended slice syntax - makes a shallow copy of the list

def reverse2(list):
    return list[::-1]

# Keeps returning the same result because the list in the variable being
# passed is not being changed when it runs. So, you get the same result
# because you are seeing the shallow copy created by the slicing operations.
