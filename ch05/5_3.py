import numpy as np

def simulate_st_petersburg(trials=10000):
    total_winnings = 0

    for _ in range(trials):
        n = 1
        while np.random.rand() > 0.5:  # 裏が出続ける間
            n += 1
        total_winnings += 2**n

    return total_winnings / trials

# 試行回数を増やすほど、平均（期待値）がどんどん跳ね上がっていきます
print(f"1,000回の平均: {simulate_st_petersburg(1000)}円")
print(f"100,000回の平均: {simulate_st_petersburg(100000)}円")
