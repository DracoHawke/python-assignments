# Q.1 Area Of Circle
# A.1 ->


def area(r):
    pi = 3.14
    area1 = (4 * pi * (r * r))
    return area1


radius = int(input('enter the radius of sphere\n'))
print('The area of circle with radius %d is %.2f' % (radius, area(radius)))


# Q.2 perfect number
# A.2 ->


def perfect():
    for j in range(1, 1001):
        sum1 = 0
        for i in range(1, int(j)):
            if j % i == 0:
                sum1 = sum1 + i
        if sum1 == j:
            print(j)


perfect()

# Q.3 Multiplication Table
# A.3 ->


def multiplication(num):
    for i in range(1, 11):
        print("%d * %d = %d" % (num, i, (num*i)))


num = int(input("enter the number you want to display multiplication table of: \n"))
multiplication(num)


# Q.4 power function
# A.4 ->


def power(num1,num2):
    if num2 == 1:
        return num1
    else:
        return pow(num1, num2)


x = int(input('enter the number'))
y = int(input('enter the exponent'))
z = power(x, y)
print('the solution for %d ^ %d is: ' % (x, y), z)
