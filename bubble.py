def bubblesort(obj1):
    n = len(obj1.array)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if obj1.array[j] > obj1.array[j + 1]:
                obj1.array[j], obj1.array[j +1] = obj1.array[j + 1], obj1.array[j]
