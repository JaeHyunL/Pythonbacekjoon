a = int(input())
# 2 + 6 = 8
# 6 + 8 = 14
# 8 + 14 = 12
# 4 +2 = 6
# 2 + 6 = 26
count = 0
first = a
while True:
    a1 = a // 10  # 몫
    a2 = a % 10  # 나머지

    a3 = (a1 + a2) % 10  # 합이야

    a = int(str(a2) + str(a3))  # 마지막
    count += 1

    if a == first:
        break
print(count)
