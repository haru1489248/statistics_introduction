import numpy as np

# 1からnまでの和
def calculate_total(n: int):
    return n * (n + 1) / 2  # (n-1) ではなく (n+1)

# 1からnまでの2乗の和
def calculate_square_total(n: int):
    return (n * (n + 1) * (2 * n + 1)) / 6

# 面数のリスト
n_list = [4, 6, 8, 12, 20]

print("=== Results ===")
for n in n_list:
    # 期待値: E(X) = (1+2+...+n) / n
    avg = calculate_total(n) / n

    # 分散: V(X) = E(X^2) - {E(X)}^2
    var = (calculate_square_total(n) / n) - (avg**2)

    print(f"{n}面体: 期待値={avg:.2f}, 分散={var:.2f}")
