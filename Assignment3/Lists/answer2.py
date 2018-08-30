x = int(input("enter the number of entries you want to make into the list \n"))
list1 = []
for i in range(0, x):
    a = input("enter list element\n")
    list1.append(a)
list2 = ['google', 'apple', 'facebook', 'microsoft', 'tesla']
list1.append(list2)
print(list1)
