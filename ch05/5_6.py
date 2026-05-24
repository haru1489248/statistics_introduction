import math
import numpy as np

# 累積分布関数 (Y = X^2)
# 「結果が y 以下になる確率」を、元の X の範囲（√y）から求めている
def cumulative_distribution(y: float):
    if y < 0:
        return 0
    elif 0 <= y <= 1:
        return math.sqrt(y)
    else:
        return 1

# 密度関数
# 累積分布関数の微分：g(y) = 1 / (2 * √y)
def density(y: float):
    # 0 < y <= 1 の範囲で定義される
    if 0 < y <= 1:
        return 1 / (2 * math.sqrt(y))
    else:
        # 範囲外（y <= 0 や y > 1）では密度は 0
        return 0

# 0から1の一様分布から100万個サンプルを取る
x = np.random.uniform(0, 1, 1000000)

# それを2乗したものの平均を出す
y_mean = np.mean(x**2)

print(f"期待値の近似値: {y_mean:.4f}") # ほぼ 0.3333 になる

y_v_mean = np.mean(x**4)

var = y_v_mean - (y_mean**2)

print(f"分散の近似値: {var:.4f}")
