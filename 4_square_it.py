import math

n = int(input())

# Method 1
square = math.pow(n, 2)
print(int(square))

# Method 2
mul = 1
for i in range(2):
    mul *= n
# print(mul)

# Test case submission link
# https://oj.masaischool.com/status/2910923d4f91c2a13a8e806855adedbd