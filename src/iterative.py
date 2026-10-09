# Діана
import numpy as np
import math
import matplotlib.pyplot as plt


def zero_diagonal(C, D):
    """x_i(1 - c_ii) = ... -> ділимо рядок на (1 - c_ii), діагональ = 0.
    Повертає (C0, d0)."""
    C0 = np.copy(C)
    d0 = np.copy(D)
    n = len(C)

    for i in range(n):
        factor = 1.0 - C[i, i]
        C0[i] = C0[i] / factor
        d0[i] = d0[i] / factor
        C0[i, i] = 0.0

    return C0, d0


def norms(C0):
    """Повертає (n1, n2, n3): max суми рядків, max суми стовпців, евклідова."""
    n1 = np.max(np.sum(np.abs(C0), axis=1))
    n2 = np.max(np.sum(np.abs(C0), axis=0))
    n3 = np.sqrt(np.sum(C0 ** 2))
    return n1, n2, n3


def get_tolerance(q, eps):
    """Допоміжна функція для обчислення порогу зупинки."""
    if q > 0.5:
        return ((1.0 - q) / q) * eps
    return eps


def jacobi(C0, d0, eps, max_iter=1000):
    """Метод простої ітерації. Старт x0 = нулі.
    Повертає (x, history), history = [[k, x1, x2, x3, x4, max_e], ...]"""
    n = len(d0)
    x = np.zeros(n)
    history = [[0] + list(x) + [None]]

    q = norms(C0)[0]
    tol = get_tolerance(q, eps)

    for k in range(1, max_iter + 1):
        x_old = x.copy()
        x = np.dot(C0, x_old) + d0

        max_e = np.max(np.abs(x - x_old))
        history.append([k] + list(x) + [max_e])

        if max_e <= tol:
            break

    return x, history


def seidel(C0, d0, eps, max_iter=1000):
    """Метод Зейделя. Старт x0 = нулі.
    Повертає (x, history), history = [[k, x1, x2, x3, x4, max_e], ...]"""
    n = len(d0)
    x = np.zeros(n)
    history = [[0] + list(x) + [None]]

    q = norms(C0)[0]
    tol = get_tolerance(q, eps)

    for k in range(1, max_iter + 1):
        x_old = x.copy()
        for i in range(n):
            x[i] = np.dot(C0[i], x) + d0[i]

        max_e = np.max(np.abs(x - x_old))
        history.append([k] + list(x) + [max_e])

        if max_e <= tol:
            break

    return x, history


def plot_convergence(histories, filename):
    """Будує графік збіжності і зберігає в filename."""
    plt.figure(figsize=(10, 6))

    for method_name, history in histories.items():
        k_vals = [row[0] for row in history[1:]]
        e_vals = [row[-1] for row in history[1:]]
        plt.semilogy(k_vals, e_vals, marker='o', label=method_name)

    plt.xlabel('Номер ітерації, k')
    plt.ylabel('Максимальна похибка, max|e|')
    plt.title('Графік збіжності ітераційних методів')
    plt.grid(True, which="both", linestyle='--')
    plt.legend()

    plt.savefig(filename)
    plt.close()



if __name__ == "__main__":
    import os
    from data import C, D, EPS

    C0, d0 = zero_diagonal(C, D)
    print("Норми:", norms(C0))

    x_j, hist_j = jacobi(C0, d0, EPS)
    x_s, hist_s = seidel(C0, d0, EPS)
    print("Проста ітерація:", np.round(x_j, 4), "ітерацій:", hist_j[-1][0])
    print("Зейдель:        ", np.round(x_s, 4), "ітерацій:", hist_s[-1][0])

    # корінь проєкту = папка на рівень вище за src
    src_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(src_dir, "convergence.png")
    plot_convergence({"Проста ітерація": hist_j, "Зейдель": hist_s}, filename)
    print("Графік збережено:", filename)
