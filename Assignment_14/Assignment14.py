from functools import *

# Question 1
# Print cube of each number in a list using list comprehension

lst = [1, 3, 4, 5, 8]
lst1 = [x**3 for x in lst]
print(lst1)

# Question 2
# Print prime number between a range of numbers
lst = [x for x in range(1, 30) if 0 not in[x% i for i in range(2, x)]]
print(lst)

# Question 3
# Difference between List Comprehension and Generator Expression

# Using Generator Expression

lst = []
for i in range(1, 6):
    lst.append(i**2)
print(lst)

# Using List Comprehension

lst = [i**2 for i in range(1, 6)]
print(lst)

# Question 4
# Convert the list into Fahernheit

celcius = [39.2, 36.5, 37.3, 37.8]
lst = list(map(lambda x: (x*1.8)+32, celcius))
print(lst)

# Question 5
# Apply an anonymous function to square all the elements of a list
Square = [1, 2, 3, 4, 5]
lst = list(map(lambda x: x**2, Square))
print(lst)

# Question 6
# Filter out all the prime numbers from the list
lst1 = [1, 23, 4, 6, 7, 9, 8, 5, 4]


def prime(n):
    for i in range(2,n):
        if n% i == 0:
            break
    else:
        return n


lst = list(filter(prime,lst1))
print(lst)

# Question 7
# Multiply all the elements of the list using reduce function


lst2 = [1, 2, 3, 4, 5]
lst = reduce(lambda x, y: x*y, lst2)
print(lst)
