# Q.1 Create user defined dictionary
# A.1 ->

dict1 = {}
i = 'a'
while i != 'end':
    key = input('enter the key value for dictionary: ')
    value = input('enter the value for corresponding key: ')
    dict1[key] = value
    i = input('enter "end" to terminate input and print dictionary otherwise anything to continue')
print(dict1)


# Q.2: nested dictionary
# A.2 ->
records = {'Rohan': {'Chemistry': 60, 'Physics': 95, 'English': 95}, 'Sarthak': {'Chemistry': 96, 'Physics': 95, 'English': 98}, 'Rishav': {'Chemistry': 92, 'Physics': 90, 'English': 90}}
name = input("Enter the name: ")
for key in records:
    if name == key:
        print(key, records[key])
