

array = [1, 4, 0, 3, 2]

n = len(array)

for i in range(1, n):

    x = array[i]

    j = i
    print(f'{x=}, {j=}, {i=}', array[j - 1])
    while j > 0 and x < array[j - 1]:
        print(array[j], array[j - 1])
        array[j] = array[j - 1]
        j -= 1
    array[j] = x
    print(array)
