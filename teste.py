hillis_array = [8, 2, 6, 4, 9, 0, 13, 7, 1, 5, 7, 3, 6, 9, 1, 2]


n = len(hillis_array)
out = hillis_array[:]
step = 0
print("-" * 25)

print(n)
print(out)
print(step)
print("-" * 25)


while (1 << step) < n:

    jump = 1 << step
    next_out = out[:]

    print("-" * 25)
    print(jump)
    print(next_out)
    print(n)
    print("-" * 25)

    for i in range(jump, n):
        print(jump)
        print(n)
        next_out[i] = out[i] + out[i - jump]
        print(next_out)

    print("-" * 25)
    out = next_out
    step += 1

print("-" * 25)
print(out)
print(step)
