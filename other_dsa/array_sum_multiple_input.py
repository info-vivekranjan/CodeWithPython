# 2
# 5
# 1 2 3 4 5
# 10
# 5 7 5 7 5 7 5 7 5 7

test_cases = input('Enter number of test_cases')

for i in range(int(test_cases)):
    n = int(input())
    arr = input()
    arr = list(map(int, arr.split(' ')))
    sum = 0
    for j in range(n):
        sum += int(arr[j])
    print (sum)
