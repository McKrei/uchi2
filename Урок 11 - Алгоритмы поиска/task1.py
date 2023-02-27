n = int(input())
array = list(map(int, input().split()))

for i in range(n - 1, 0, -1):
    index_max = 0
    for j in range(0, i + 1):
        if array[j] > array[index_max]:
            index_max = j
    array[i], array[index_max] = array[index_max], array[i]
    print(*array)
