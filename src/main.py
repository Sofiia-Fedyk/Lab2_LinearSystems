#Софія
import numpy as np
from data import A, b, C, D, EPS
from output import print_solution, print_iterations, print_summary, print_matrix
from cramer import solve_cramer
from inverse import solve_inverse
from gauss import solve_gauss
from lu import solve_lu
from iterative import zero_diagonal, norms, jacobi, seidel

results = []


def run_exact(name, func):
    try:
        x = func(A, b)
    except NotImplementedError:
        print(f"\n[{name}] ще не реалізовано")
        return
    print_solution(name, x)
    print(f"  нев'язка max|Ax-b| = {np.max(np.abs(A @ x - b)):.2e}")
    print(f"  numpy.linalg.solve: {np.round(np.linalg.solve(A, b), 4)}")
    results.append({"method": name, "x": x, "iters": None})


print("ЗАВДАННЯ 1")
print_matrix(A, "A =")
run_exact("Крамер", solve_cramer)
run_exact("Гаусс (гол. елемент)", solve_gauss)
run_exact("Матричний", solve_inverse)
run_exact("LU-розклад", solve_lu)

print("\nЗАВДАННЯ 2")
try:
    C0, d0 = zero_diagonal(C, D)
    print_matrix(C0, "C (нулі на діагоналі) =")
    print("d =", np.round(d0, 4))
    n1, n2, n3 = norms(C0)
    print(f"||C||1 = {n1:.4f}, ||C||2 = {n2:.4f}, ||C||3 = {n3:.4f}")
    for name, func in [("Проста ітерація", jacobi), ("Зейдель", seidel)]:
        x, hist = func(C0, d0, EPS)
        print_iterations(name, hist)
        print_solution(name, x)
        results.append({"method": name, "x": x, "iters": hist[-1][0]})
except NotImplementedError:
    print("\n[Завдання 2] ще не реалізовано")

print_summary(results)
