def calculate_gini(data, label):
    """平均差とジニ係数を計算して表示する"""
    n = len(data)
    results = []
    for i in data:
        for j in data:
            results.append(abs(i - j))
    
    mean_diff = sum(results) / (n**2)
    average = sum(data) / n
    gini = sum(results) / (2 * n**2 * average)
    
    print(f"{label} answer")
    print(f"平均差：{mean_diff}")
    print(f"average {label}: {average}")
    print(f"ジニ係数：{gini}")
    print()

if __name__ == "__main__":
    A = [0, 3, 3, 5, 5, 5, 5, 7, 7, 10]
    B = [0, 1, 2, 3, 5, 5, 7, 8, 9, 10]
    C = [3, 4, 4, 5, 5, 5, 5, 6, 6, 7]
    
    calculate_gini(A, "A")
    calculate_gini(B, "B")
    calculate_gini(C, "C")
