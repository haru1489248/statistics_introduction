import numpy as np

# 一様分布の密度関数
def uniform_distribution(range: tuple, x: float):
    if range[0] <= x <= range[1]:
        return 1 / (range[1] - range[0])
    else:
        return 0

# [0, 1]の一様分布を作成
p = np.arange(0, 1, 0.1)
# 平均
mu = np.mean(p)
# 分散
V = np.mean((p - mu)**2)
# 標準偏差
D = np.sqrt(V)
# 歪度
a_3 = np.mean((p - mu)**3) / D**3
# 尖度
a_4 = np.mean((p - mu)**4) / D**4

print(f"歪度: {a_3}")
print(f"尖度: {a_4}")
