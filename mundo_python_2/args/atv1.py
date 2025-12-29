def somatoria(*content):
    total = 0
    for a in content:
        total += a
    return total

def main():
    import re
    content = list(map(int, re.split(r'[, ]+', input().strip())))
    result = somatoria(*content)
    print(result)

if __name__ == "__main__":
    main()