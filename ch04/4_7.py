# P(A|C)
p_a_given_c = 0.95

# P(A|C^c)
p_a_given_not_c = 0.05

# P(C)
p_c = 0.005

# P(C^c)
p_not_c = 1 - p_c

# ベイズの定理
p_c_given_a = (
    p_a_given_c * p_c
) / (
    p_a_given_c * p_c +
    p_a_given_not_c * p_not_c
)

print(p_c_given_a)
