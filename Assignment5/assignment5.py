# Q.1 check if user input is leap year or not
# A.1 ->

print('enter the year to check')
year = int(input())
if year % 4 == 0:
    print('year mentioned IS leap year')
else:
    print('year input IS NOT a leap year')

# Q.2 check if square or rectangle
# A.2 ->

print('\n\n')
print('enter the 2 sides of the desired parallelogram')
side1 = int(input())
side2 = int(input())
if side1 == side2:
    print('the parallelogram with desired sides is a SQUARE')
else:
    print('the parallelogram with desired sides is a RECTANGLE')

# Q.3  oldest and youngest
# A.3 ->

print('\n\n')
print('enter the required ages of the 3 people')
age1 = int(input())
age2 = int(input())
age3 = int(input())
if age1 >= age2 and age1 >= age3:
    old = age1
elif age2 >= age1 and age2 >= age3:
    old = age2
else:
    old = age3
if age1 <= age2 and age1 <= age3:
    young = age1
elif age2 <= age1 and age2 <= age3:
    young = age2
else:
    young = age3
print('person with age %d is oldest', old)
print('person with age %d is youngest', young)

# Q.4   WORK AREA
# A.4 ->

print('\n\n')
print("enter the applicant's age, sex(m/f), and marital status(y/n)")
age1 = int(input())
sex = input()
m_s = input()
if sex == 'f' or sex == 'F':
    print('as a FEMALE, applicant is only has access to URBAN AREA WORK')
elif sex == 'm' or sex == 'M':
    if 20 < age1 < 40:
        print('as a MALE with age %d, applicant has access to WORK ANYWHERE' % age1)
    elif 40 < age1 < 60:
        print('as a MALE with age %d, applicant has access to WORK ANYWHERE' % age1)
else:
    print('INVALID INPUT')

# Q.5 COST
# A.5 ->

print('\n\n')
print('enter the number of units you want to purchase, each unit costs 100, you get discount for units worth 1000')
units = int(input())
discount = int(units / 10) * 100
cost = (units * 1000) - discount
print('your final cost is %d with %d discount that was implemented' % (cost, discount))

# ''''''' LOOPS '''''''

# Q.1 INPUT 10 INT AND PRINT
# A.1 ->

print('\n\n')
n = []
print('enter 10 numbers to be displayed on screen')
for i in range(0, 10):
    a = int(input())
    n.append(a)
for i in range(0, 10):
    print('no: ', n[i])

# Q.2 INFINITE LOOP
# A.2 ->

print('\n\n')
i = 1
#while i > 0:
#    print('infinite')
print("remove the above given two '#' for an infinite loop")

# Q.3 LIST2 CONTAINS SQUARE OF ELE OF LIST1
# A.3 ->

print('\n\n')
print('enter the list elements and type -1 for ending input of list 1')
l1 = []
l2 = []
i = int(input())
while i != -1:
    l1.append(i)
    i = int(input())
for i in range(0, len(l1)):
    a = int(l1[i] * l1[i])
    l2.append(a)
print(l1)
print(l2)

# Q.4 list with int,float,str and store then separately
# A.4 ->

print('\n\n')
print('enter the list elements')
l1 = []
lint = []
lflt = []
lstr = []
i = 'a'
while str(i) != 'end':
    i = input()
    l1.append(i)
    print("to end entering in list enter 'end' otherwise enter next element")
    i = input()
for i in range(0, len(l1)):
    if l1[i].isalpha():
        lstr.append(l1[i])
    elif l1[i].isdecimal():
        lflt.append(l1[i])
    elif l1[i].isnumeric():
        lint.append(l1[i])
print('original list: ', l1)
print('int list: ', lint)
print('float list: ', lflt)
print('string list: ', lstr)

# Q.5 using range (1,101) for prime numbers
# A.5 ->

print('\n\n')
l1 = []
for i in range(1, 101):
    flag = True
    for j in range(2, int(i/2)+1):
        if i % j == 0:
            flag = False
            continue
    if flag:
        l1.append(i)
print(l1)

# Q.6 PRINT PATTERN
# A.6 ->

print('\n\n')
for i in range(1, 6):
    print('*' * i)

# Q.7 USER LIST, DELETING ELE USING FOR
# A.7 ->

print('\n\n')
print('enter the list elements and type "end" for ending input of list 1')
l1 = []
i = input()
while i != 'end':
    l1.append(i)
    i = input()
test = input('enter the element you want to search and delete\n')
count = len(l1)
for i in range(0, count):
    if l1[i] == test:
        del l1[i]
        count -= 1
print(l1)
