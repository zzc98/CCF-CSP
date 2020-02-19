def main():
    y = int(input())
    d = int(input())
    if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
        dic = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30,
               7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    else:
        dic = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
               7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    for i in range(1, 13):
        if d <= dic[i]:
            print(i)
            print(d)
            break
        else:
            d -= dic[i]


if __name__ == "__main__":
    main()
