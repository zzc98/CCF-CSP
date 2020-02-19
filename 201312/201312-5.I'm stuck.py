class Point:
    def __init__(self, row, col, mark):
        self.row = row
        self.col = col
        self.mark = mark


s = input().split()
r, c = int(s[0]), int(s[1])
maze = []
stop = []
for i in range(0, c+2):
    stop.append(Point(0, i, '#'))
maze.append(stop)
start_point, flag_position = (), ()
start_set = set()
for i in range(1, r+1):
    road = [Point(i, 0, '#')]
    s = input()
    for j in range(1, c+1):
        m = s[j-1]
        p = Point(i, j, m)
        road.append(p)
        if m == 'S':
            start_point = p
            start_set.add((i, j))
        elif m == 'T':
            flag_position = ((i, j))
    road.append(Point(i, c+1, '#'))
    maze.append(road)
stop = []
for i in range(0, c+2):
    stop.append(Point(r+1, i, '#'))
maze.append(stop)

# start
start_queue = [start_point]
while len(start_queue) != 0:
    head = start_queue.pop(0)
    if head.mark == '-':
        p = maze[head.row][head.col - 1]
        s = (head.row, head.col - 1)
        if p.mark != '#' and s not in start_set:
            start_set.add(s)
            start_queue.append(p)
        p = maze[head.row][head.col + 1]
        s = (head.row, head.col + 1)
        if p.mark != '#' and s not in start_set:
            start_set.add(s)
            start_queue.append(p)
    elif head.mark == '|':
        p = maze[head.row-1][head.col]
        s = (head.row-1, head.col)
        if p.mark != '#' and s not in start_set:
            start_set.add(s)
            start_queue.append(p)
        p = maze[head.row+1][head.col]
        s = (head.row+1, head.col)
        if p.mark != '#' and s not in start_set:
            start_set.add(s)
            start_queue.append(p)
    elif head.mark == '.':
        p = maze[head.row+1][head.col]
        s = (head.row+1, head.col)
        if p.mark != '#' and s not in start_set:
            start_set.add(s)
            start_queue.append(p)
    elif head.mark == '+' or head.mark == 'S' or head.mark == 'T':
        p = maze[head.row][head.col - 1]
        s = (head.row, head.col - 1)
        if p.mark != '#' and s not in start_set:
            start_set.add(s)
            start_queue.append(p)
        p = maze[head.row][head.col + 1]
        s = (head.row, head.col + 1)
        if p.mark != '#' and s not in start_set:
            start_set.add(s)
            start_queue.append(p)
        p = maze[head.row-1][head.col]
        s = (head.row-1, head.col)
        if p.mark != '#' and s not in start_set:
            start_set.add(s)
            start_queue.append(p)
        p = maze[head.row+1][head.col]
        s = (head.row+1, head.col)
        if p.mark != '#' and s not in start_set:
            start_set.add(s)
            start_queue.append(p)


if flag_position not in start_set:
    print("I'm stuck!")
else:
    ans = []
    for t in start_set:
        task_point = maze[t[0]][t[1]]
        task_queue = [task_point]
        task_set = {t}
        while len(task_queue) != 0:
            head = task_queue.pop(0)
            if head.mark == '-':
                p = maze[head.row][head.col - 1]
                s = (head.row, head.col - 1)
                if p.mark != '#' and s not in task_set:
                    task_set.add(s)
                    task_queue.append(p)
                p = maze[head.row][head.col + 1]
                s = (head.row, head.col + 1)
                if p.mark != '#' and s not in task_set:
                    task_set.add(s)
                    task_queue.append(p)
            elif head.mark == '|':
                p = maze[head.row-1][head.col]
                s = (head.row-1, head.col)
                if p.mark != '#' and s not in task_set:
                    task_set.add(s)
                    task_queue.append(p)
                p = maze[head.row+1][head.col]
                s = (head.row+1, head.col)
                if p.mark != '#' and s not in task_set:
                    task_set.add(s)
                    task_queue.append(p)
            elif head.mark == '.':
                p = maze[head.row+1][head.col]
                s = (head.row+1, head.col)
                if p.mark != '#' and s not in task_set:
                    task_set.add(s)
                    task_queue.append(p)
            elif head.mark == '+' or head.mark == 'S' or head.mark == 'T':
                p = maze[head.row][head.col - 1]
                s = (head.row, head.col - 1)
                if p.mark != '#' and s not in task_set:
                    task_set.add(s)
                    task_queue.append(p)
                p = maze[head.row][head.col + 1]
                s = (head.row, head.col + 1)
                if p.mark != '#' and s not in task_set:
                    task_set.add(s)
                    task_queue.append(p)
                p = maze[head.row-1][head.col]
                s = (head.row-1, head.col)
                if p.mark != '#' and s not in task_set:
                    task_set.add(s)
                    task_queue.append(p)
                p = maze[head.row+1][head.col]
                s = (head.row+1, head.col)
                if p.mark != '#' and s not in task_set:
                    task_set.add(s)
                    task_queue.append(p)
        # print(t,maze[t[0]][t[1]].mark, task_set)
        if flag_position not in task_set:
            ans.append(t)

    # ans = start_set.difference(task_set)
    # print(start_set)
    # print(task_set)
    # print(start_set - task_set)
    print(len(ans))

"""
5 5
--+-+
..|#.
..|##
S-+-T
####.


2

"""