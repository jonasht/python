import lippy as lp
c_vec = [6, 6, 6]
a_matrix = [
    [4,    1,  1],
    [1,    2,  0],
    [0,  0.5,  4]
    ]

b_vec = [5, 3, 8]

simplex = lp.SimplexMethod(c_vec, a_matrix, b_vec)
solution, func_value = simplex.solve()

print('=-'*30)
print(solution)
print()
print(func_value)
print('=-'*30)
