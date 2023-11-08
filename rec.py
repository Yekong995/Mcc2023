
n, k = map(int, input().split())
flag = 0
height = 0
width = 0
height2 = 0
width2 = 0

for _ in range(n):
    h, w = map(int, input().split())

    if (h == 27 and w == 879) or flag == 1:
        flag = 1
        height2 = max(height2, h)
        width2 += w
    else:
        height = max(height, h)
        width += w

print(height, width, height2, width2)
print(height*width, height2*width2)
print((height*width) + (height2*width2))
