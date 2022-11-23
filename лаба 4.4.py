....
Группа 21-ис21 Подгорнова Александра Васильевна 15.11.22.
Задание 4.
Даны три числа. Найти сумму двух наибольших из них.
....
n1=float(input())  
 n2=float(input())  
 n3=float(input())  
 if n1<n2 and n1<n3: 
     print(n2+n3) 
 elif n2<n1 and n2<n3: 
     print(n1+n3) 
 else: 
     print(n1+n2)