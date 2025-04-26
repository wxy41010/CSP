def simulate_balls(n, L, t, initial_positions):
    # 初始化位置和速度数组，1表示向右，-1表示向左
    positions = initial_positions.copy()  # 当前位置
    velocities = [1] * n  # 初始速度都向右
    # 模拟t秒
    for _ in range(t):
        # 更新每个小球的位置
        for i in range(n):
            positions[i] += velocities[i]  # 根据速度更新位置
            # 检查边界反弹
            if positions[i] == 0:  # 到达左端点
                velocities[i] = 1  # 速度变为向右
            elif positions[i] == L:  # 到达右端点
                velocities[i] = -1  # 速度变为向左
        # 检查两球碰撞
        for i in range(n):
            for j in range(i + 1, n):
                if positions[i] == positions[j]:  # 如果两球位置相同，发生碰撞
                    velocities[i], velocities[j] = -velocities[i], -velocities[j]  # 交换速度方向
    return positions
n, L, t = map(int, input().split())  # 读取n, L, t
initial_positions = list(map(int, input().split()))  # 读取初始位置
# 计算t秒后的位置
result = simulate_balls(n, L, t, initial_positions)
print(*result)