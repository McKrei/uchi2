array = [1, 4, 0, 3, 2]
n = len(array)

for i in range(n - 1):
    for j in range(n - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
        print(array)

print(array)


