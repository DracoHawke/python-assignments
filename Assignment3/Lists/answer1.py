# import simplejson
x = int(input("enter the number of entries you want to make into the list \n"))
list1 = []
for i in range(0, x):
    a = input("enter list element\n")
    list1.append(a)
print(list1)
# f = open('output_answer1.txt', 'w')
# simplejson.dump(list1, f)
# f.close()
