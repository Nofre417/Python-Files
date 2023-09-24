def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i < pivot]
    greather = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greather)

print(quick_sort([1, 53, 6, 24, 75, 22, 76]))