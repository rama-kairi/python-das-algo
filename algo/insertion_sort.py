import random


def insertion_sort(el: list) -> list:
    for i in range(1, len(el)):
        j = i
        while j > 0 and el[j] < el[j - 1]:
            el[j], el[j - 1] = el[j - 1], el[j]
            j -= 1
    return el


if __name__ == "__main__":
    num_list = [2, 4, 3, 5, 1]

    print(insertion_sort(num_list))
