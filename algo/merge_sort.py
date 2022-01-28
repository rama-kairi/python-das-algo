def merge_sort(el: list):
    if len(el) <= 1:
        return el
    mid = len(el) // 2
    left = merge_sort(el[:mid])
    right = merge_sort(el[mid:])
    return merge(left, right)


def merge(left: list, right: list):
    sorted_list = []
    while left and right:
        if left[0] <= right[0]:
            sorted_list.append(left.pop(0))
        else:
            sorted_list.append(right.pop(0))
    sorted_list += left
    sorted_list += right
    return sorted_list


# Merge sort with key and reverse
def merge_sort_key(el: list, key=lambda x: x, reverse=False):
    if len(el) <= 1:
        return el
    mid = len(el) // 2
    left = merge_sort_key(el[:mid])
    right = merge_sort_key(el[mid:])
    return merge_key(left, right, key, reverse)


def merge_key(left: list, right: list, key=lambda x: x, reverse=False):
    sorted_list = []
    while left and right:
        if key(left[0]) <= key(right[0]):
            sorted_list.append(left.pop(0))
        else:
            sorted_list.append(right.pop(0))
    sorted_list += left
    sorted_list += right
    return sorted_list[::-1] if reverse else sorted_list


if __name__ == "__main__":
    print(merge_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
    print(
        merge_sort_key(
            [1, 3, 5, 7, 9, 2, 4, 6, 8, 0], key=lambda x: x % 2
        )
    )
    print(
        merge_sort_key(
            [1, 3, 5, 7, 9, 2, 4, 6, 8, 0],
            key=lambda x: x % 2,
            reverse=True,
        )
    )
