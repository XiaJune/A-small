def swap(a, b):
    sum_a = sum(a)
    sum_b = sum(b)
    diff = sum_a - sum_b
    while True:
        best_i, best_j, best_change = 0, 0, 0
        for i in range(len(a)):
            for j in range(len(b)):
                change = a[i] - b[j]
                if abs(diff - 2 * change) < abs(diff - 2 * best_change):
                    best_change = change
                    best_i = i
                    best_j = j
        if best_change == 0:  # 差已经不能再减小
            return False
        a[best_i], b[best_j] = b[best_j], a[best_i]
        sum_a -= best_change
        sum_b += best_change
        diff = sum_a - sum_b


a = [100, 99, 98, 1, 2, 3]
b = [1, 2, 3, 4, 5, 40]
print(sum(a) - sum(b))
swap(a, b)
print(a, b, sum(a) - sum(b))