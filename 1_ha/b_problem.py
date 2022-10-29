def selection_sort(x):
    N = len(x)
    for i in range(N - 1):
        i_min = i
        for j in range(i + 1, N):
            if x[i_min] > x[j]:
                i_min = j
        x[i], x[i_min] = x[i_min], x[i]


if __name__ == '__main__':
    N = int(input())
    x = []

    for i in range(N):
        num, name, score = input().split()
        x.append((-(int(score)), int(num), str(name)))

