def combination(m, n):
    # 实现C(m,n)组合数计算
    # m <= n
    # return n!/(n-m)!/m!
    return factorial(n-m, n) // factorial(0, m)


def factorial(m, n):
    # 实现阶乘 n! / m!
    # m <= n
    # return n! / m!
    ans = 1
    while n - m > 0:
        ans *= n
        n -= 1
    return ans


if __name__ == '__main__':
    n = int(input())
    ans = 0
    for count01 in range(2, n-1):
        count23 = n - count01
        # 用count01和count23分别记下0，1和2，3的个数
        # 由于0,1,2,3至少各有一个所以count01的范围是2到n-2
        ans += combination(count01, n) * (count01 - 1) * (count23 - 1)
    print(int((ans//2) % 1000000007))

