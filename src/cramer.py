#Софія
import numpy as np
from output import print_vector


def det(M):
    """Власний визначник (рекурсивний розклад за першим рядком)."""
    n = M.shape[0]
    if n == 1:
        return M[0, 0]
    if n == 2:
        return M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0]
    total = 0.0
    for j in range(n):
        if M[0, j] == 0:
            continue
        minor = np.delete(M[1:], j, axis=1)
        total += (-1) ** j * M[0, j] * det(minor)
    return total


def solve_cramer(A, b, verbose=False):
    """Повертає x (np.ndarray, 4 елементи)."""
    A = A.copy()
    delta = det(A)
    if abs(delta) < 1e-12:
        raise ValueError("Δ = 0: метод Крамера не застосовний")
    n = A.shape[0]
    deltas = np.empty(n)
    for j in range(n):
        Aj = A.copy()
        Aj[:, j] = b
        deltas[j] = det(Aj)
    if verbose:
        print(f"Δ = {delta:.4f}")
        print_vector(deltas, "Δ1..Δ4 =")
    return deltas / delta


if __name__ == "__main__":
    from data import A, b
    print(solve_cramer(A, b, verbose=True))  # очікується [5, -10, 3, -5]
