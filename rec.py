
n, k = map(int, input().split())
height = 0
width = 0

for _ in range(n):
    h, w = map(int, input().split())

    height = max(height, h)
    width += w

print(height*width)
