hillis_array = [8, 2, 6, 4, 9, 0, 13, 7, 1, 5, 7, 3, 6, 9, 1, 2]


def hillis_steele_scan(values):
    n = len(values)
    out = values[:]
    step = 0

    while (1 << step) < n:
        jump = 1 << step
        next_out = out[:]
        for i in range(jump, n):
            next_out[i] = out[i] + out[i - jump]
        out = next_out
        step += 1

    return out


print(hillis_steele_scan(hillis_array))