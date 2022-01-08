# 12 8 5 6 3
# You are given the numbers of 1 runs, 2 runs, 3 runs, fours and sixes scored by a batsman. Your task is  to compute total run scored by that batsman.
arr = input()

lst = list(map(int, arr.split(' ')))
onse = lst[0]
twos = lst[1]
threes = lst[2]
fours = lst[3]
sixs = lst[4]

total = onse + twos*2 + threes*3 + fours*4 + sixs*6
print(total)

# Test cases
# https://oj.masaischool.com/status/5bd421ec6a482cbd78bb14853b679ecf 