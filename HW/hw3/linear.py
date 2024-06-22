# 使用chatGPTg生成

from scipy.optimize import linprog

# 目標函數係數 (需要最小化 -3x - 2y - 5z 以達到最大化 3x + 2y + 5z)
c = [-3, -2, -5]

# 不等式左邊的係數矩陣 (Ax <= b)
A = [
    [1, 1, 0],
    [2, 0, 1],
    [0, 1, 2]
]

# 不等式右邊的常數向量
b = [10, 9, 11]

# 變數的邊界 (0 <= x, 0 <= y, 0 <= z)
x_bounds = (0, None)
y_bounds = (0, None)
z_bounds = (0, None)

# 使用linprog解決線性規劃問題
res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds, z_bounds], method='highs')

# 打印結果
if res.success:
    print('Optimal value:', -res.fun)
    print('x:', res.x[0])
    print('y:', res.x[1])
    print('z:', res.x[2])
else:
    print('No solution found:', res.message)
