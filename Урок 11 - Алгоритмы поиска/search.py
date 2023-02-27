array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(array)
x = 9

for i in range(n):
    if x == array[i]:
        print(i)
        break
else:
    print(-1)
    