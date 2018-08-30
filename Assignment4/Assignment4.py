import copy as c

# Q.1 - Reverse the whole list using list methods.
# A.1 ->

num = int(input("Enter the number of elements\n"))
print("Enter the elements")
list1 = []
for i in range(0, num):
    ele = int(input())
    list1.append(ele)
print(list1)
print("Reversed list is: ")
list1.reverse()
print(list1)

# Q.2 - Print all the uppercase letters from a string.
# A.2 ->

print("enter string")
str1 = input()
final_str = ""
for i in str1:
    if i.isupper():
        final_str = final_str + i
print("characters in upperCase are: ", final_str)

# Q.3 - Split the user input on comma's and store the values in a list as integers
# A.3 ->

str1 = input("Enter the numbers with commas in between\n")
list1 = []
list1 = str1.split(",")
print("List : ", list1)

# Q.4 - Check whether a string is palindromic or not.
# A.4 ->

print("Enter a string")
str1 = input()
rev = "".join(reversed(str1))
print("str1: ", str1, "rev: ", rev)
if str1 == rev:
    print("String is Palindrome")
else:
    print("String is not Palindrome")

# Q.5- Make a deepcopy of a list and write the difference between shallow copy and deep copy.
# A.5(a) ->
# DeepCopy

list1 = [1, 2, [3, 4, 5], 6, 7, 8, 9, 10]
list2 = c.deepcopy(list1)
print('List 1: ', list1)
print('List 2(deepcopy of list 1): ', list2)
list2[2][1] = 11
print('After changing List 2')
print('List 1: ', list1)
print('List 2(deepcopy of list 1): ', list2)
print(" ")

# A.5(b) ->
# ShallowCopy

list1 = [1, 2, [3, 4, 5], 6, 7, 8, 9, 10]
list2 = c.copy(list1)
print('List 1: ', list1)
print('List 2(Shallow copy of list 1): ', list2)
list2[2][1] = 11
list2[2][2] = 12
print('After changing List 2')
print('List 1: ', list1)
print('List 2(Shallow copy of list 1): ', list2)

# DIFFERENCE

# Changes made in deep copy of a list are never reflected in the original list
# where as changes made in shallow copy of a list are always reflected in original list.
# In deep copy copy of object is copied to other object where as in shallow copy
# reference of object is copied in other object
