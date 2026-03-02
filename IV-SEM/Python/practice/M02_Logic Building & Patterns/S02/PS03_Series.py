'''
Docstring for IV-SEM.Python.practice.M02_Logic Building & Patterns.S02.PS03_Series
Fibonacci Series:
'''
n=int(input())
f1,f2=0,1
for i in range(n):
    print(f1,end=" ")
    f1,f2=f2,f1+f2

#using list
fib=[0,1]
for i in range(2,n):
    fib.append(fib[i-1] + fib[i-2])
for i in fib:
    print(i,end=" ")
'''
power of  
'''