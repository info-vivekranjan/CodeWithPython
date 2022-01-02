# You are provided price of three different types of ticket: 1st Class, 2nd class and 3rd class.

# Also, you know the number of tickets of each type you need to book. Find total cost you need to pay.

# 1200 1400 2000
# 5 6 2


cost = input()
cost = list(map(int, cost.split(' ')))
quantity = input()
quantity = list(map(int, quantity.split(' ')))

total = (cost[0] * quantity[0]) + (cost[1] * quantity[1]) + (cost[2] * quantity[2])
print(total)

# Tset cases
# https://oj.masaischool.com/status/94c317dde26b7488a9081e03973e4528