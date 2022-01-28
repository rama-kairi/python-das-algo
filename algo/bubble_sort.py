def bubble_sort(el: list) -> list:
    """
    Bubble sort algorithm

    :param el: list of el to sort
    :return: sorted

    Big O: O(n^2)
    """
    for i in range(len(el)):
        swapped = False
        for j in range(len(el) - 1, i, -1):
            if el[j] < el[j - 1]:
                el[j], el[j - 1] = (
                    el[j - 1],
                    el[j],
                )
                swapped = True
        if not swapped:
            break
    return el


if __name__ == "__main__":
    el = [5, 4, 3, 2, 1]
    country_names = [
        "Russia",
        "Canada",
        "United States",
        "China",
        "Brazil",
        "India",
        "Australia",
        "France",
    ]
    print(bubble_sort(country_names))
