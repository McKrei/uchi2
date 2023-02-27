def merge_sort(array):

    if len(array) == 1:  # если в массиве 1 элемент, то он отсортирован
        return array

    left = merge_sort(array[: len(array) // 2])  # запускаем сортировку левой части
    right = merge_sort(array[len(array) // 2:])  # запускаем сортировку правой части
    
    result = []
    l, r = 0, 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:  # выбираем из какой части забрать элемент
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    if l >= len(left):  # прицепляем оставшуюся часть оставшегося массива
        result += right[r:]
    else:
        result += left[l:]
    return result


array = [1, 4, 0, 3, 2]
print(merge_sort(array))
