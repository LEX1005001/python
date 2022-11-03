num=int(input("Введите число: "))
sum=0 # Cумама чисел
count=0
count0=0
while num!=0:
    d=num%10
    num//10
    count+=1
    sum+=d
if d==0:
    count0+=1
print("Сумма чисел: ",sum)
print("Колличество чисел: ",count)
print("Среднее арифм: ",sum/count)
print("Колличество нулей в числе: ",count0)