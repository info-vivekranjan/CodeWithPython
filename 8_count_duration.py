# 2
# 1 44 2 14
# 2 42 8 23
import math
test_cases = int(input())


for i in range(test_cases):
    arr = input()
    arr = list(map(int, arr.split(' ')))
    SH, SM, EH, EM = arr
    SH = SH * 60
    total_start = SH + SM
    EH = EH * 60
    total_end = EH + EM
    total_diff = total_end - total_start
    total_hour = math.floor(total_diff / 60)
    total_min = total_diff % 60
    print (f"{total_hour} {total_min}")

# Test Cases
# https://oj.masaischool.com/status/2cebe6c0d9f53c538af84c1c33645228
