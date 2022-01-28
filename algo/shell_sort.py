def shell_sort(el: list) -> list:
    """
    Shell sort
    """
    gap = len(el) // 2
    while gap > 0:
        for i in range(gap, len(el)):
            temp = el[i]
            j = i
            while j >= gap and el[j - gap] > temp:
                el[j] = el[j - gap]
                j -= gap
            el[j] = temp
        gap //= 2
    return list(set(el))


if __name__ == "__main__":
    print(shell_sort([5, 2, 4, 6, 1, 3, 2]))
