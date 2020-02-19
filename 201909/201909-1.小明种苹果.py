def main():
    string = input().split()
    tree, roll = int(string[0]), int(string[1])
    ops = []
    for i in range(tree):
        ops.append(input())
    total = 0
    max_shu = 0
    index = -1
    for i in range(tree):
        op = ops[i].split()
        temp = 0
        for j in range(1, roll+1):
            temp += int(op[j])
        if temp < max_shu:
            max_shu = temp
            index = i
        total += int(op[0]) + temp
    print(total, index+1, max_shu*(-1))


if __name__ == "__main__":
    main()

"""
3 3
73 -8 -6 -4
76 -5 -10 -8
80 -6 -15 0

2 2
10 -3 -1
15 -4 0

"""