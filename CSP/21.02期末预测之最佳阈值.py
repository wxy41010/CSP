m = int(input())
data = [list(map(int, input().split())) for _ in range(m)]
# 获取所有可能的阈值（去重并排序）
thresholds = sorted(set(y for y, _ in data))
# 定义函数：计算某个阈值的正确预测次数
def count_correct(theta):
    correct = 0
    for y, result in data:
        # 根据阈值预测
        prediction = 0 if y < theta else 1
        # 如果预测正确，计数加1
        if prediction == result:
            correct += 1
    return correct
# 寻找最佳阈值
max_correct = -1  # 最大正确次数
best_theta = -1   # 最佳阈值
for theta in thresholds:
    correct = count_correct(theta)
    # 如果当前正确次数更大，或者正确次数相等但阈值更大，更新最佳阈值
    if correct > max_correct or (correct == max_correct and theta > best_theta):
        max_correct = correct
        best_theta = theta
print(best_theta)