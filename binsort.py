import random

n = 10
a = [random.randint(1,20) for i in range(n)]

def insert(a):
    x = [0] * (2 * n + 1)
    left = n
    right = n
    x[n - 1] = a[0]
    for i in range(1, n):
        t = a[i]
        if t >= a[0]:
            right += 1
            j = right - 1
            while j > 0 and t < x[j - 1]:
                x[j] = x[j - 1]
                j -= 1
            x[j] = t
        else:
            left -= 1
            j = left - 1
            while j < 2 * n - 1 and t > x[j + 1]:
                x[j] = x[j + 1]
                j += 1
            x[j] = t
    for j in range(n):
        a[j] = x[j + left - 1]

if __name__ == "__main__":
    print('отсортированные числа')
    insert(a)
    print(a)