def main():
    num = int(input())
    coordinates = []
    for i in range(num):
        x, y = input().split(' ')
        coordinates.append((int(x), int(y)))

    x_dict = {}
    for item in coordinates:
        if item[0] in x_dict:
            x_dict[item[0]].append(item[1])
        else:
            x_dict[item[0]] = [item[1]]

    score_num = [0, 0, 0, 0, 0]
    for item in coordinates:
        try:
            if item[1] in x_dict[item[0]-1] and item[1] in x_dict[item[0]+1] and (item[1]+1) in x_dict[item[0]] and (item[1]-1) in x_dict[item[0]]:
                score = 0
                if item[1]+1 in x_dict[item[0]-1]:
                    score += 1
                if item[1]+1 in x_dict[item[0]+1]:
                    score += 1
                if item[1]-1 in x_dict[item[0]-1]:
                    score += 1
                if item[1]-1 in x_dict[item[0]+1]:
                    score += 1
                score_num[score] += 1
        except:
            continue

    for i in score_num:
        print(i)


if __name__ == "__main__":
    main()
