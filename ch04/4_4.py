r_list = [5, 10, 15, 20, 21, 22, 23, 24, 25, 30, 35, 40, 50, 60]

results = []
for r in r_list:
    p = 1
    for i in range(1, r):
        p *= (1 - (i / 365))
    results.append(1-p)
    print("="*10)
    print(f"{r}の結果:", 1-p)
    print("="*10)
