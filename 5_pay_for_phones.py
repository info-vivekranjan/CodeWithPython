# 10000 20000 15000 5000
# 2 3 4 3

price = input()
price = list(map(int, price.split(' ')))

p1,p2,p3,p4 = price

n = input()
n = list(map(int, n.split(' ')))

n1,n2,n3,n4 = n

total = p1*n1 + p2*n2 + p3*n3 + p4*n4
total = int(total)

if total<= 150000:
    print('Possible')
else:
    print('Not Possible')


# Test cases after submissions:
# https://oj.masaischool.com/status/ea2f0f58605a83ce5a80a00d002dd49c
