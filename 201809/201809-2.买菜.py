def main():
    n = int(input())
    ab = []
    for i in range(n):
        s = input().split()
        ab.append((int(s[0]), int(s[1])))
    cd = []
    for i in range(n):
        s = input().split()
        cd.append((int(s[0]), int(s[1])))
    ans = 0
    i, j = 0, 0
    while i < n and j < n:
        if cd[j][1] == ab[i][1]:
            ans += ab[i][1] - max(ab[i][0], cd[j][0])
            i += 1
            j += 1
        elif cd[j][1] > ab[i][1]:
            if cd[j][0] < ab[i][1]:
                ans += ab[i][1] - max(ab[i][0], cd[j][0])
            i += 1
        else:
            if cd[j][1] > ab[i][0]:
                ans += cd[j][1] - max(ab[i][0], cd[j][0])
            j += 1

    return ans


if __name__ == "__main__":
    ans = main()
    print(ans)

"""
4
1 3
5 6
9 13
14 15
2 4
5 7
10 11
13 14
"""