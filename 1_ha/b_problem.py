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
        num, score, name = input().split()
        x.append((-(int(score)), int(num), str(name))) # add '-' score to reverse selection_sort order (from increase to decrease),
                                                       # if scores of elements are equal then 'num' will be sorted in increse order (like in task statement)

    selection_sort(x)

    for name in x[:3]:
        print(name[2])
    print(*list(num[1] for num in x), sep=' ') # Q: what is *? (splat operator)
