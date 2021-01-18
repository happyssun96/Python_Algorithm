def find_name(a):
    n = len(a)
    result = set()

    for i in range(0, n-1):
        for j in range(i+1, n):
            if a[i] != a[j]:
                result.add(a[i])
    return result


def print_pairs(a):
    n = len(a)
    for i in range(0, n-1):
        for j in range(i+i, n):
            print(a[i], "-", a[j])
name = ["Tom", "Jerry", "Mike"]
print_pairs(name)
print()

