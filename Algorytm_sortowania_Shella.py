def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j   - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

# Przykład użycia:
arr = [12, 34, 54, 2, 3]
print("Lista przed sortowaniem Shella:", arr)
shell_sort(arr)
print("Lista po sortowaniu Shella:", arr)