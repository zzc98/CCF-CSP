class Ball:
    def __init__(self, position, num, direction=1):
        self.position = position
        self.num = num
        self.direction = direction

    def setDirection(self, dir):
        self.direction = dir


def main():
    s = input().split()
    length, L, time = int(s[0]),  int(s[1]),  int(s[2])
    string = input().split()
    ball = [Ball(int(string[i]), i, 1) for i in range(length)]
    if length == 1:
        for _ in range(time):
            ball[0].position += ball[0].direction
            if ball[0].position == 0:
                ball[0].setDirection(1)
                # ball[0].direction == 1
            elif ball[0].position == L:
                ball[0].setDirection(-1)
                # ball[0].direction == -1
        print(ball[0].position)
        return
    ball.sort(key=lambda item: item.position)
    for _ in range(time):
        # 移动
        for ba in ball:
            ba.position += ba.direction
        # 方向
        # 0号球
        if ball[0].position == 0:
            ball[0].setDirection(1)
            # ball[0].direction == 1
        for i in range(1, length):
            if ball[i].position == ball[i-1].position:
                ball[i-1].setDirection(ball[i-1].direction*(-1))
                ball[i].setDirection(ball[i].direction*(-1))
        # 最后一个球
        if ball[-1].position == L:
            ball[-1].setDirection(-1)
            # ball[-1].direction == -1
        # for b in ball:
        #     print(b.position, end=' ')
        # input()
    ball.sort(key=lambda item: item.num)
    for b in ball:
        print(b.position, end=' ')


if __name__ == "__main__":
    main()
