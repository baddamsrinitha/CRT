'''
sample input : 1234
sample output : 4

sample input : 455786
sample output : 6

sample input : 45
sample output : 2
'''
'''
n = int(input())
count = 0
while n > 0:
    count += 1
    n = n // 10 
print(count)
print(len(str(n)))

n = int(input())
s = 0
while n > 0:
    s += n % 10
    n = n // 10
print(s)

print(sum(map(int,str(temp))))
'''

'''
input : 12345
output : 2 3
input: 5588
output : 2 2 
'''
'''
n = int(input())
even = odd = 0
while n > 0:
    if (n % 2) == 0:
        even += 1
    else:
        odd += 1
    n //= 10
print(even, odd)
'''

'''
input : 546
output : 6 
input : 783
output : 9
546 ==> 15 ==> 6
'''
n = int(input())
while n > 9:
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    n = s
print(n)
