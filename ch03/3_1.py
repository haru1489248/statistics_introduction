import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
votes_data = np.array([41.4, 76.3, 59.2, 51.8, 52.5, 53.2, 62.4, 55.0, 57.7])
home_ownership_rate = np.array([52.8, 71.2, 72.6, 63.7, 81.3, 81.8, 70.9, 74.0, 73.2])

# 散布図を表示する
plt.xlabel("自民党得票率 (%)")
plt.ylabel("持ち家比率 (%)")
plt.title("1983年総選挙での自民党得票率と持ち家比率")
plt.scatter(x=votes_data, y=home_ownership_rate)
plt.show()

# 相関係数を計算する
x_bar = np.mean(votes_data)
y_bar = np.mean(home_ownership_rate)

# 共分散を計算する
covariance = 0
for x, y in zip(votes_data, home_ownership_rate):
    covariance += (x-x_bar)*(y-y_bar)

# それぞれの標準偏差を計算する
def calculate_standard_deviation(avg: np.float32, data: np.ndarray) -> np.ndarray:
    total = 0
    for i in data:
        total += (i - avg) ** 2

    return np.sqrt(total)

S_x = calculate_standard_deviation(avg=x_bar, data=votes_data)
S_y = calculate_standard_deviation(avg=y_bar, data=home_ownership_rate)

# 相関係数
r = covariance / (S_x * S_y)
print("相関係数:", r)
