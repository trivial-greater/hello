from scipy.optimize import linprog

# 最大化：3x + 2y
# linprog 默认求最小值，所以目标系数取负数
c = [-3, -2]

# 约束条件：
# 2x + y <= 18
# 2x + 2y <= 24
A_ub = [
    [2, 1],
    [2, 2]
]
b_ub = [18, 24]

result = linprog(
    c,
    A_ub=A_ub,
    b_ub=b_ub,
    bounds=[(0, None), (0, None)],
    method="highs"
)

if result.success:
    print("最优解：")
    print(f"x = {result.x[0]:.2f}")
    print(f"y = {result.x[1]:.2f}")
    print(f"最大目标值 = {-result.fun:.2f}")
else:
    print("没有找到可行解")
