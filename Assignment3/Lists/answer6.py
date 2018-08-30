A = [1, 66, 909, 2, 55, 24, 67, 100]
B = [22, 9, 967, 45, 80]
counteven = 0
countodd = 0
A.sort()
B.sort()
C = []
C = A.copy()
for i in range(0, B.__len__()):
    C.append(B[i])
C.sort()
for i in range(0, C.__len__()):
    if C[i] % 2 == 0:
        counteven += 1
    else:
        countodd += 1
print("no. of even elements in list: ", counteven, "\nno. of odd elements in list: ", countodd)
