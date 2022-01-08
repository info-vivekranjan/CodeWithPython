import math

n = int(input())

if n == 0:
    print("-1")
else:

    tot = 32/n

    tot = math.floor(tot)

    if tot == 0:
        print("Too Low")
    elif tot<0:
        print("-1")
    else:
        print(tot)

# Test cases link
# https://oj.masaischool.com/status/d0b1e0e2b18eec1f5955f2cdbcbcd4a5