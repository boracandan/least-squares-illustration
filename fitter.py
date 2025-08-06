from typing import Iterable, Tuple
import numpy as np


def polynomial_approximation(dataPoints: Iterable[Tuple[float, float]], n: int) -> np.ndarray:
    xPoints = np.array([p[0] for p in dataPoints], dtype=float)
    yPoints = np.array([p[1] for p in dataPoints], dtype=float)
    # Matrix with x-values
    A = np.column_stack([xPoints**degree for degree in range(n+1)])
    # Vector with y-values
    pseudoInvA = np.linalg.pinv(A)

    # Coefficient Vector
    c = pseudoInvA @ yPoints

    return c
