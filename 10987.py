a = list(map(str, input()))
count = 0
for i in a:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        count += 1
print(count)
