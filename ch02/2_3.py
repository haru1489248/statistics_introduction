import numpy as np

def calculate_entropy(data, label):
    """エントロピーを計算して表示する"""
    # 合計を1にする（確率分布にする）
    prob = data / np.sum(data)
    # エントロピーの計算 (H = -Σ p * log10(p))
    # 統計では基本的に常用対数を使用する
    entropy = -np.sum(prob * np.log10(prob))
    print(f"{label} エントロピー: {entropy}")
    return entropy

if __name__ == "__main__":
    this_year = np.array([32, 19, 10, 24, 15], dtype='f')
    ten_years_ago = np.array([28, 13, 18, 29, 12], dtype='f')

    calculate_entropy(this_year, "今年")
    calculate_entropy(ten_years_ago, "10年前")
