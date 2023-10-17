#Напишите программу, которая проверяет, что для заданного четырехзначного числа выполняется следующее соотношение: 
#сумма первой и последней цифр равна разности второй и третьей цифр
num = 1614 #int(input())
#n1 = num % 10 #4 
#n2 = num % 100 // 10 # 3
#n3 = num // 100 % 10 # 2
#n4 = num // 1000 #1
if (num // 1000)+(num % 10) == (num // 100 % 10)-(num % 100 // 10):
    print('ДА')
else:
    print('НЕТ')
#print(n1,n2,n3,n4)

a = 1234#int(input())
b1 = int(str(a)[0])
b2 = int(str(a)[1])
b3 = int(str(a)[2])
b4 = int(str(a)[3])
#print(b1,b2,b3,b4)
if b1+b4 == b2-b3:
    print ('ДА')
else:
    print ('НЕТ')


n = int(input())
d1 = (n // 10 ** 3) % 10
d2 = (n // 10 ** 2) % 10
d3 = (n // 10 ** 1) % 10
d4 = (n // 10 ** 0) % 10
if d1 + d4 == d2 - d3:
    print("ДА")
else:
    print("НЕТ")

a,b,c,d = input()
print('ДА' if int(a) + int(d) == int(b) - int(c) else 'НЕТ')    