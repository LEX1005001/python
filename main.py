from random import(randint)

matrix=[]
size=4
for i in range(size):
    row=[]
    for j in range(size):
        row.append(randint(0,10))
    matrix.append(row)
for i in range (size):
    for j in range(size):
        print(matrix[i][j],end=" ")
    print()
print("Среднее арифм: ")
for i in range(size):
    print((int(sum(matrix[i])))/size) #Cреднее арифм
print("Колл-во 0 в строке: ")
for i in range(size):
    print(matrix.count(0))
