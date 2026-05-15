import random
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib

data_1 = np.array([i for i in range(1, 31)])
data_2 = np.array([1, 5, 2, 3, 6, 7, 15, 8, 4, 11, 10, 14, 18, 13, 22, 24, 16, 19, 30, 9, 25, 17, 26, 23, 12, 20, 28, 21, 27, 29])
n = len(data_1)

r_list = []
for i in range(200):
    indices = [random.randint(1, 11) for _ in range(11)]

    random_data_1 = [data_1[i] for i in indices]
    random_data_2 = [data_2[i] for i in indices]

    random_data_1_bar = np.mean(random_data_1)
    random_data_2_bar = np.mean(random_data_2)

    covariance = np.sum((random_data_1 - random_data_1_bar) * (random_data_2 - random_data_2_bar))

    S_x = np.sqrt(np.sum((random_data_1 - random_data_1_bar)**2))
    S_y = np.sqrt(np.sum((random_data_2 - random_data_2_bar)**2))

    r = covariance / (S_x * S_y)
    r_list.append(round(r.item(), 4))
    print(f"{i+1}番目の相関係数:", r)

print(r_list)

# ヒストグラムを描画
plt.hist(r_list, bins=20, edgecolor='black') # binsは棒の数

plt.xlabel('相関係数')
plt.ylabel('頻度')
plt.title('ブートストラップ法による相関係数の分布（n=200）')

plt.show()
