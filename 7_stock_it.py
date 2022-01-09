floor_for_one_week = 5*110
rice_for_one_week = 2*120
suger_for_one_week = 2 * 42
pulse_for_one_week = 3*53
bread_for_one_week = 2 * 40
milk_for_one_week = 5*32
oil_for_one_week = 2*126

n = int(input())

arr = input()
arr = list(map(int, arr.split(' ')))

p1, p2, p3, p4, p5, p6, p7 = arr

total_for_n_week = p1*floor_for_one_week + p2*rice_for_one_week + p3*suger_for_one_week + \
    p4*pulse_for_one_week + p5*bread_for_one_week + \
    p6*milk_for_one_week + p7*oil_for_one_week

total_for_n_week = n * total_for_n_week

print(total_for_n_week)


# Test cases
# https://oj.masaischool.com/status/82c131104f9e9855d17d00c96e7a4b3f
