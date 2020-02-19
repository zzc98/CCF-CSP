def main():
    def valid(c):
        if c % 7 == 0 or '7' in str(c):
            return True
        else:
            return False

    n = int(input())  # n是总共要报的数字数目（不含跳过的数字）
    index = 1  # index是下一个人要报的数字
    skip = [0, 0, 0, 0]
    while n > 0:
        if valid(index):
            skip[index % 4-1] += 1
        else:
            n -= 1
        index += 1
    for i in skip:
        print(i)


if __name__ == "__main__":
    main()
