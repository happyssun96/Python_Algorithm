def find_max(a):
    n = len(a)
    max_index = 0
    for i in range(1, n):
        if a[i] > a[max_index]:
            max_index = i
    return max_index

def find_min(b):
    n = len(b)
    min_b = b[0]
    for i in range(1, n):
        if b[i] < min_b:
            min_b = b[i]
    return min_b

v = [17, 92, 18, 33, 58, 7, 33, 42]

print(find_max(v))

print(find_min(v))