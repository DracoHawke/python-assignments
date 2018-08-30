import random

# Q.1 Read n lines
# A.1 ->

f = open('test.txt', 'r')               # file open operation for f1
lines = f.readlines()
n = int(input('enter the number of lines you want to print from the end'))
print(lines[:n])

# Q.2 frequency
# A.2 ->

f = open('testq2.txt')
line = f.read()
split = line.split()
print(split)


# Q.3 copy the contents of a file to another file
# A.3 ->

f2 = open('output.txt', 'w')
for l in lines:
    f2.write(l)
f2.close()                              # file close operation for f2

# Q.4 combine each line from first file with the corresponding line in second file
# A.4 ->

f2 = open('output q3.txt', 'a')
f3 = open('test2.txt', 'r')
for l in lines:
    li = f3.readline()
    f2.write(l + li)                    # note(important) ==  that the write concatenation does not ignore \n and also concatenate it
f2.close()
f3.close()

# Q.5 random generation, writing, sorting, and printing
# A.5 ->

f2 = open('test q5.txt', 'w')
for i in range(0, 100):
    s = str(random.randint(0, 1000)) + '\n'
    f2.write(s)
f2.close()
f3 = open('output q5.txt', 'r+')
f2 = open('test q5.txt', 'r')
e_line = f2.read()
e = e_line.split()
e.sort()
f3.write(str(e))
f2.close()
f3.seek(0)
print(f3)

# note that sorting in this program happens in context to string data type not integer
