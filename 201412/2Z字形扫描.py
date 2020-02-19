def main():
    dim = int(input())
    matrix = []
    for i in range(dim):
        s = input().split()
        matrix.append(s)
    ans = []
    for row in range(dim):
        t = []
        i, j = row, 0
        while i >= 0:
            t.append(matrix[i][j])
            i -= 1
            j += 1
        ans.append(t)
    for col in range(1, dim):
        t = []
        i, j = dim - 1, col
        while j < dim:
            t.append(matrix[i][j])
            i -= 1
            j += 1
        ans.append(t)
    for i in range(2*dim-1):
        if i % 2 == 1:
            ans[i].reverse()
        for a in ans[i]:
            print(a, end=' ')


if __name__ == "__main__":
    main()
