import numpy as np
import matplotlib.pyplot as plt
import math

# 1. サンプリングによる可視化
x = np.random.uniform(0, 1, 100000) # 元の一様分布
y = x**2 # 2乗に変換

# 2. 理論上の密度関数
y_vals = np.linspace(0.01, 1, 100) # 0除算を避けるため0.01から
g_y = 1 / (2 * np.sqrt(y_vals))

# プロット
plt.figure(figsize=(10, 6))

# ヒストグラム（実データの密度）
# densityがTrueで密度関数にできる（面積の合計が1になる）
plt.hist(y, bins=100, density=True, alpha=0.3, color='blue', label='Simulated Data (Y=X^2)')

# 理論式（g(y) = 1/2√y）
plt.plot(y_vals, g_y, color='red', lw=2, label='Theoretical PDF: $g(y) = 1/(2\sqrt{y})$')

plt.title("Probability Density of $Y = X^2$")
plt.xlabel("y")
plt.ylabel("Density")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
