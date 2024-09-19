from ortools.sat.python import cp_model
import numpy as np
import time

G = [(1, 8, 2), (2, 2, 2), (2, 7, 5), (3, 3, 7), (3, 6, 3), (3, 7, 4), (4, 1, 2), (4, 4, 1), (4, 7, 3), (4, 8, 4),
     (5, 1, 6), (5, 2, 4), (5, 5, 8), (5, 8, 5), (5, 9, 9), (6, 2, 9), (6, 3, 5), (6, 6, 2), (6, 9, 1), (7, 3, 3),
     (7, 4, 4), (7, 7, 8), (8, 3, 9), (8, 8, 1), (9, 2, 1)]


sol = np.zeros((9, 9), dtype=int)
start = time.time()
model = cp_model.CpModel()

# Variables
x = {}  # x[i, j, k] is 1 if cell in row i, column j contains number k+1


for i in range(9):
    for j in range(9):
        for k in range(9):
            x[i, j, k] = model.NewIntVar(0, 1, f'x_{i}_{j}_{k}')

# Constraints
# Each cell contains exactly one number
for i in range(9):
    for j in range(9):
        model.Add(sum(x[i, j, k] for k in range(9)) == 1)

# Each number appears exactly once in each row
for i in range(9):
    for k in range(9):
        model.Add(sum(x[i, j, k] for j in range(9)) == 1)

# Each number appears exactly once in each column
for j in range(9):
    for k in range(9):
        model.Add(sum(x[i, j, k] for i in range(9)) == 1)

# Each number appears exactly once in each 3x3 subgrid

for i in range(3):
    for j in range(3):
        for k in range(9):
            model.Add(sum(x[3*i+di, 3*j+dj, k] for di in range(3) for dj in range(3))  == 1)

# Initial values
for i, j, k in G:
    model.Add(x[i-1, j-1, k-1] == 1)
        

# Solve
solver = cp_model.CpSolver()
status = solver.Solve(model)

if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print(f'''Solution found in {solver.WallTime()} seconds''')
    for i in range(9):
        for j in range(9):
            for k in range(9):
                if solver.Value(x[i, j, k]) == 1:
                    sol[i, j] = k+1
                    break
    print(sol)
else:
    print("No solution found.")