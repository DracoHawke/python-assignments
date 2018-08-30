import re as r

# Q.1: Email Validation
# A.1 ->

email = input("enter the email that needs to be verified: ")
matcher = r.finditer('^[a-z][a-zA-Z0-9]*[@](gmail.com|yahoo.com)', email)   # using finditer to find instances of given pattern
count = 0
for i in matcher:
    count += 1
if count == 1:
    print('given email is in correct format')
else:
    print('email input is not of correct format')


# Q.2: validate indian phone number
# A.2 ->

pno = input('enter the phone number in format "country code" followed by "-" and then the "phone number": ')
matcher = r.finditer('^[+][9][1][-][6-9][\d]{9}', pno)
count = 0
for i in matcher:
    count += 1
if count == 1:
    print('phone number input is A INDIAN PHONE NUMBER')
else:
    print('phone number input is NOT A INDIAN PHONE NUMBER')

# ^[+][9][1][6-9][\d]{9}                                phone number
# ^[a-zA-Z_][a-zA-Z\d_]*                                variable declaration
# ^[a-z][a-zA-Z0-9]*[@](gmail.com|yahoo.com)            email verification
