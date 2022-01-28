# Write a Binary Search Algorithm


number_list = list(range(1, 1000000))


def linear_search(
    number_list, number_to_find
):  # sourcery skip: use-any
    for number in number_list:
        if number == number_to_find:
            return True
    return False


# print(linear_search(number_list, 999999808))


def binary_search(number_list, number_to_find):
    low = 0
    high = len(number_list) - 1

    while low <= high:
        mid = (low + high) // 2
        num_list_mid = number_list[mid]
        if num_list_mid == number_to_find:
            return True
        elif num_list_mid < number_to_find:
            low = mid + 1
        else:
            high = mid - 1
    return False


def binary_search_recursive(number_list, number_to_find):
    nll = len(number_list)
    if nll == 0:
        return False
    mid = nll // 2
    if number_list[mid] == number_to_find:
        return True
    if number_to_find < number_list[mid]:
        return binary_search_recursive(
            number_list[:mid], number_to_find
        )
    else:
        return binary_search_recursive(
            number_list[mid + 1 :], number_to_find
        )


print(binary_search_recursive(number_list, 999990))
