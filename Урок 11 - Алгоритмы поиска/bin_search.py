array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(array)
x = 9

left = 0
right = n
while left < right:
    mid = (left + right) // 2
    if array[mid] == x:
        print(mid)
        break
    elif array[mid] < x:
        left = mid + 1
    else:
        right = mid
else:
    print(-1)