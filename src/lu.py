#Вільгельм
import numpy as np

import numpy as np
from output import print_matrix


def leading_minors(A):
    """Обчислює та повертає головні мінори матриці."""
    n = A.shape[0]
    minors = []
    for i in range(1, n + 1):
        # np.linalg.det використовуємо як виняток за умовою
        minor_val = np.linalg.det(A[:i, :i])
        minors.append(np.round(minor_val, 4))
    return minors


def lu_decompose(A):
    """Виконує LU-розклад матриці (метод Дулітла: одиниці на діагоналі L)."""
    n = A.shape[0]
    L = np.eye(n)  # Матриця з одиницями на головній діагоналі
    U = np.zeros((n, n))  # Нульова матриця для U

    for i in range(n):
        # 1. Знаходимо елементи верхнього трикутника (для матриці U)
        for j in range(i, n):
            sum_u = np.sum(L[i, :i] * U[:i, j])
            U[i, j] = A[i, j] - sum_u

        # 2. Знаходимо елементи нижнього трикутника (для матриці L)
        for j in range(i + 1, n):
            sum_l = np.sum(L[j, :i] * U[:i, i])
            # Формула вимагає ділення на діагональний елемент U
            L[j, i] = (A[j, i] - sum_l) / U[i, i]

    return L, U


def solve_lu(A, b, verbose=False):
    """Розв'язує САР через LU-розклад."""
    A_copy = np.copy(A).astype(float)
    b_copy = np.copy(b).astype(float)
    n = len(b_copy)

    # Крок 1: Перевірка мінорів
    if verbose:
        minors = leading_minors(A_copy)
        print(f"Головні мінори: {minors}")

    # Крок 2: LU-розклад
    L, U = lu_decompose(A_copy)

    if verbose:
        print_matrix(L, "Матриця L:")
        print_matrix(U, "Матриця U:")

    # Крок 3: Прямий хід (Ly = b)
    # Оскільки на діагоналі L стоять одиниці, ділити на L[i,i] не потрібно
    y = np.zeros(n)
    for i in range(n):
        y[i] = b_copy[i] - np.sum(L[i, :i] * y[:i])

    if verbose:
        print_matrix(y, "Вектор y:")

    # Крок 4: Зворотний хід (Ux = y)
    # Тут на діагоналі U стоять числа, тому ділимо на U[i,i]
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.sum(U[i, i + 1:] * x[i + 1:])) / U[i, i]

    return x


if __name__ == "__main__":
    from data import A, b

    print_matrix(solve_lu(A, b, verbose=True), "Вектор розв'язків x (LU):")

def lu_decompose(A):
    """Повертає (L, U) за формулами (11) з методички."""
    raise NotImplementedError


def solve_lu(A, b, verbose=False):
    """Ly = b, потім Ux = y. Повертає x (np.ndarray)."""
    raise NotImplementedError


if __name__ == "__main__":
    from data import A, b
    print(solve_lu(A, b, verbose=True))  # очікується [5, -10, 3, -5]
    print(solve_lu(A, b, verbose=True))  # очікується [5, -10, 3, -5]
