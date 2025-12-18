lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lst2 = []
for num in lst:
    if num % 2 == 0:
        lst2.append(num)

print(sum(lst2))