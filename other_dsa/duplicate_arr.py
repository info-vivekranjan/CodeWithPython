n = int(input('Enter n: '))
# arr = ['vivek', 'bhargav', 'vivek','raj']

arr = input('Enter array: ')
arr = list(arr.split(' '))
arr.sort()

for i in range(n):
        if arr[i] == arr[i+1]:
            print(arr[i])
            break