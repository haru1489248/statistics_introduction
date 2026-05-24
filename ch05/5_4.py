import numpy as np

# 適当なデータ (例: 0, 1, 2, 3, 4)
X = np.array([0, 1, 2, 3, 4])
mu = np.mean(X) # 2.0

def calculate_mse(data, a):
    return np.mean((data - a)**2)

# 平均値 (2.0) と、それ以外の値 (1.5 や 2.5) で比較
print(f"a=2.0 (平均) のとき: {calculate_mse(X, 2.0)}") # 最小
print(f"a=1.5 のとき: {calculate_mse(X, 1.5)}")
print(f"a=2.5 のとき: {calculate_mse(X, 2.5)}")
