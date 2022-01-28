import random


def quick_sort(el: list) -> list:
    if len(el) <= 1:
        return el
    pivot = el[0]
    less = [i for i in el[1:] if i <= pivot]
    greater = [i for i in el[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == "__main__":
    num_list = [random.randint(0, 100) for _ in range(100)]

    print(quick_sort(num_list))
