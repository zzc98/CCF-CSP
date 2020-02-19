n = int(input())
draw = set()
for _ in range(n):
    s = input().split()
    x1, y1, x2, y2 = int(s[0]), int(s[1]), int(s[2]), int(s[3])
    for y in range(y1, y2):
        for x in range(x1, x2):
            draw.add((x+0.5, y+0.5))
print(len(draw))
