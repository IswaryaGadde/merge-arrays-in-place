def merge_arrays_inplace(array1, array2):
    # Compare the last elements of array1 and array2
    i = len(array1) - len(array2) - 1
    j = len(array2) - 1

    # Iterate over each element in array2
    for k in range(len(array2) - 1, -1, -1):
        if i >= 0 and array1[i] < array2[k]:
            array1[i + k + 1] = array2[k]
            i -= 1
        else:
            array1[i + k + 1] = array1[i]
            i -= 1

# Example usage:
array1 = [1, 3, 5, 7, 9, 0, 0, 0, 0, 0]  # Ensure array1 has enough space
array2 = [2, 4, 6, 8, 10]

merge_arrays_inplace(array1, array2)

print("Merged Array (in-place):", array1)
