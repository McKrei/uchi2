def quick_sort(array):
    if len(array) < 1:  # если в массиве 1 элемент или нет элементов
        return array
    pivot = array[len(array) // 2]  # находим опорный элемент
    left, center, right = [], [], []
    for el in array:  # заполняем левую и правую часть
        if el < pivot:
            left.append(el)
        elif el > pivot:
            right.append(el)
        else:
            center.append(el)
    return quick_sort(left) + center + quick_sort(right) # сортируем левую и правую части и объединяем результат


array = [1, 4, 0, 3, 2]
print(quick_sort(array))
