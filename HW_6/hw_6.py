# binary search
def binary_search(arr: [int], number: int):
    index_result = -1
    if number not in arr or arr is None:
        return index_result
    if len(arr) == 1:
        index_result = 0

    if len(arr) > 1:
        index_min = 0
        index_max = len(arr) - 1
        while index_min <= index_max:
            index_middle = index_min + int((index_max - index_min) / 2)
            if number == arr[index_middle]:
                return index_middle
            elif number > arr[index_middle]:
                index_min = index_middle + 1
            else:
                index_max = index_middle - 1
    return index_result


if __name__ == '__main__':
    arr = [12, 14, 22, 24, 25, 26, 43, 47, 50, 51, 55]
    print(binary_search(arr, 26))
