def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpiont = (first + last) // 2
        if list[midpiont] == target:
            return midpiont
        elif list[midpiont] < target:
            first = midpiont + 1
        else:
            last = midpiont - 1
    return None


def verify(index):
    if index is not None:
        print(f"target found at index : {index}")
    else:
        print("Target not found in list")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = binary_search(numbers, 10)
verify(result)
