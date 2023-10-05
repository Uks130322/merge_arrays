def merge_arrays(arr1, arr2):
    """Merge two sorted arrays into one"""

    arr3 = []
    if arr1[0] >= arr1[-1]:
        arr1.reverse()
    if arr2[0] >= arr2[-1]:
        arr2.reverse()
    index_1 = 0
    index_2 = 0
    while index_1 < len(arr1) or index_2 < len(arr2):
        if 0 < index_1 < len(arr1) and arr1[index_1] == arr1[index_1 - 1]:
            index_1 += 1
            continue
        if 0 < index_2 < len(arr2) and arr2[index_2] == arr2[index_2 - 1]:
            index_2 += 1
            continue
        if index_1 < len(arr1) and index_2 < len(arr2):
            if arr1[index_1] == arr2[index_2]:
                arr3.append(arr1[index_1])
                index_1 += 1
                index_2 += 1
                continue
        if index_1 < len(arr1) and (index_2 >= len(arr2) or
                                    arr1[index_1] < arr2[index_2]):
            arr3.append(arr1[index_1])
            index_1 += 1
        elif index_2 < len(arr2):
            arr3.append(arr2[index_2])
            index_2 += 1
    return arr3
