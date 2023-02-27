n = int(input())
array = [int(n) for n in input().split()]
x = int(input())
left = 0
right = n

while left < right:
    mid = (left + right) // 2
    if array[mid] < x:
        left = mid + 1
    elif array[mid] > x:
        right = mid
    else:
        if mid == 0 or array[mid - 1] != x:
            print(mid)
            break
        else:
            right = mid
else:
    print(-1)
