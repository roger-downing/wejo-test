my_list = []
for n in range(2, 1000):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        my_list.append(n)

print(my_list)
