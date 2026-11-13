def find_dominator(arr):
    length = 0
    for _ in arr:
        length += 1

    result = -1
    for candidate in arr:
        count = 0
        for number in arr:
            if number == candidate:
                count += 1
        if count > length / 2:
            result = candidate

    return result


print(find_dominator([3, 4, 3, 2, 3, 1, 3, 3]))
print(find_dominator([1, 2, 3, 4]))
print(find_dominator([]))