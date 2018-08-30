A = [1, 66, 909, 2, 55, 24, 67, 100]
B = [22, 9, 967, 45, 80]
A.sort()
B.sort()
C = []
C = A.copy()
for i in range(0, B.__len__()):
    C.append(B[i])
C.sort()
print(C)
