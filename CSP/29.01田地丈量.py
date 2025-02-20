n, a, b = map(int, input().split())
area = 0
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    # 计算田地与 (0,0) - (a,b) 的相交部分
    x1, y1, x2, y2 = max(0, x1), max(0, y1), min(a, x2), min(b, y2)
    area += (x2-x1) * (y2-y1)
print(area)
"""
4 10 10
0 0 5 5
5 -2 15 3
8 8 15 15
-2 10 3 15

44
"""