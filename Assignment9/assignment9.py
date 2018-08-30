# Q.1 -> Zero Division Error
# A.1->


try:
    a = 3
    if a < 4:
        a = a/(a-3)
        print(a)
except ZeroDivisionError:
    print("You Cannot Divide By Zero")


# Q.2 -> INDEX ERROR
# A.2 ->


try:
    li = [1, 2, 3]
    print(li[3])
except IndexError:
    print("Please Enter an Index which is less than {}".format(len(li)))


# Q.3 -> Tell The output

try:
    raise NameError("Hi there")
except NameError:
    print("An exception")
    raise
# The output Of the Following Code is "An Exception"


# Q.4 -> Tell the output
# A.4 ->

def AbyB(a, b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print("a/b result in 0")
    else:
        print(c)


# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

# Output of The above Code
# The Result is
# -5.0
# a/b result in 0


# Q.5 ->
# Write a program to show and handle following exceptions:
# 1. Import Error
# 2. Value Error
# 3. Index Error

# The Following Code is for Import Error
try:
    import nmb
except ImportError:
    print("Please Import Valid Module")


# The Following Code is for showing and handling Value Error
try:
    a = int(input("Enter a Number "))
    # We Encounter an Indexerrorif we enter an string value in the variable
except:
    print("Please Enter a valid Number")


# The Following code is for handling IndexError
try:
    li = [4, 5, 6]
    print(li[4])
except IndexError:
    print("Please Enter A valid Index")
