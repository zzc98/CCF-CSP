def main():
    string = input().split()
    data = [int(s) for s in string]

    total = 0
    last = 1
    for num in data:
        if num == 0:
            break
        elif num == 1:
            last = 1
            total += 1
        else:
            if last == 1:
                last = 2
            else:
                last += 2
            total += last
    print(total)

if __name__ == "__main__":
    main()