import numpy as np

data_1 = np.array([i for i in range(1, 31)])
data_2 = np.array([1, 5, 2, 3, 6, 7, 15, 8, 4, 11, 10, 14, 18, 13, 22, 24, 16, 19, 30, 9, 25, 17, 26, 23, 12, 20, 28, 21, 27, 29])
n = len(data_1)

# スピアマン（これは今のコードでOK）
r_s = 1 - (6 / (n**3 - n)) * np.sum((data_1 - data_2) ** 2)
print(f"スピアマンの順位相関係数: {r_s:.4f}")

# ケンドールの順位相関係数
G = 0 # 正の組 (concordant pairs)
H = 0 # 負の組 (discordant pairs)

for i in range(n):
    for j in range(i + 1, n):
        # data_1 の大小関係を確認
        order_1 = data_1[i] - data_1[j]
        # data_2 の大小関係を確認
        order_2 = data_2[i] - data_2[j]

        # 両方の符号が一致していれば「正の組」
        if order_1 * order_2 > 0:
            G += 1
        # 符号が逆（一方が正で他方が負）なら「負の組」
        elif order_1 * order_2 < 0:
            H += 1

# ケンドールのタウの公式: (G - H) / (n * (n - 1) / 2)
r_k = (G - H) / (n * (n - 1) / 2)
print(f"ケンドールの順位相関係数: {r_k:.4f}")

# (答え合わせ) scipyを使う場合
from scipy.stats import kendalltau
print(f"Scipyでの結果: {kendalltau(data_1, data_2)[0]:.4f}")
