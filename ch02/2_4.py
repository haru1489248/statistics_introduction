import numpy as np

def calculate_scores(data, label):
    """標準得点(Z)と偏差値(T)を計算して表示する"""
    mu = np.mean(data)
    sigma = np.std(data)
    
    # 標準得点 (Z = (x - μ) / σ)
    z_scores = (data - mu) / sigma
    # 偏差値 (T = Z * 10 + 50)
    t_scores = z_scores * 10 + 50
    
    print(f"--- {label} ---")
    print(f"元のデータ: {data}")
    print(f"標準得点(Z): {z_scores}")
    print(f"偏差値(T):   {t_scores}")
    print()
    return z_scores, t_scores

if __name__ == "__main__":
    this_year_data = np.array([32, 19, 10, 24, 15], dtype='f')
    ten_years_ago_data = np.array([28, 13, 18, 29, 12], dtype='f')
    
    calculate_scores(this_year_data, "今年")
    calculate_scores(ten_years_ago_data, "10年前")
