#Софія
import numpy as np


def print_matrix(M, title=""):
    if title:
        print(title)
    for row in np.atleast_2d(M):
        print("  " + "  ".join(f"{v:10.4f}" for v in row))


def print_solution(method, x):
    print(f"\n=== {method} ===")
    for i, v in enumerate(x, 1):
        print(f"  x{i} = {v:.4f}")


def print_iterations(method, history):
    # history: список рядків [k, x1, x2, x3, x4, max_e]
    print(f"\n=== {method}: ітерації ===")
    print(f"{'k':>3} " + " ".join(f"{'x'+str(i):>9}" for i in range(1, 5)) + f" {'max|e|':>10}")
    for k, *xs, e in history:
        e_str = "---" if e is None else f"{e:.6f}"
        print(f"{k:>3} " + " ".join(f"{v:9.4f}" for v in xs) + f" {e_str:>10}")


def print_summary(results):
    # results: список словників {"method", "x", "iters"}
    print("\n=== Порівняльна таблиця ===")
    print(f"{'Метод':<22}" + "".join(f"{'x'+str(i):>10}" for i in range(1, 5)) + f"{'Ітерацій':>10}")
    for r in results:
        it = "---" if r["iters"] is None else str(r["iters"])
        print(f"{r['method']:<22}" + "".join(f"{v:10.4f}" for v in r["x"]) + f"{it:>10}")


def print_vector(v, title=""):
    if title:
        print(title)
    print("  " + "  ".join(f"{x:10.4f}" for x in v))
