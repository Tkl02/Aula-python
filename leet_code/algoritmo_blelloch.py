blelloch_array = [8, 2, 6, 4, 9, 0, 13, 7, 1, 5, 7, 3, 6, 9, 1, 2]


def blelloch_scan(values):
    if not values:
        return []

    n = len(values)
    size = 1
    while size < n:
        size *= 2

    work = list(values) + [0] * (size - n)

    step = 1
    while step < size:
        for i in range(0, size, 2 * step):
            right = i + 2 * step - 1
            left = i + step - 1
            work[right] += work[left]
        step *= 2

    work[size - 1] = 0

    step = size // 2
    while step >= 1:
        for i in range(0, size, 2 * step):
            right = i + 2 * step - 1
            left = i + step - 1
            left_val = work[left]
            work[left] = work[right]
            work[right] += left_val
        step //= 2

    return work[:n]


if __name__ == "__main__":
    result = blelloch_scan(blelloch_array)
    print("entrada:", blelloch_array)
    print("scan exclusiv:", result)
