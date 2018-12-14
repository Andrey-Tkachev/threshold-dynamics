import numpy as np
from math import pow

class SplineInterpolation(object):

    def __init__(self, grid):
        if grid is not None:
            if len(grid) < 2:
                raise ValueError

            self._grid = np.array(sorted(grid))
        else:
            self._grid = None

        self._tau = None
        self._m = None
        self._a = None
        self._b = None

    def load_from_dict(self, backup: dict):
        self._tau = np.array(backup['tau'])
        self._m = np.array(backup['m'])
        self._a = np.array(backup['a'])
        self._b = np.array(backup['b'])
        self._grid = np.array(backup['grid'])
        return self

    def dump_to_dict(self):
        return {
            'tau': self._tau.tolist(),
            'm': self._m.tolist(),
            'a': self._a.tolist(),
            'b': self._b.tolist(),
            'grid': self._grid.tolist(),
        }

    def _calc_coefs(self):
        N = self._grid.shape[0] - 1  # segments from 0 to N overall N + 1 points
        self._tau = np.diff(self._grid[:, 0].flatten())
        self._m = np.zeros(N + 1)
        self._a = np.zeros(N + 1)
        self._b = np.zeros(N + 1)

        f = self._grid[:, 1].flatten()

        A = np.zeros(N - 1)
        B = np.zeros(N - 1)
        C = np.zeros(N - 1)
        D = np.zeros(N - 1)

        for i in range(N - 1):
            D[i] = (
                (f[i + 2] - f[i + 1]) / self._tau[i + 1] -
                (f[i + 1] - f[i]) / self._tau[i]
            )

        for i in range(N - 1):
            B[i] = (self._tau[i] + self._tau[i + 1]) / 3.
            if i > 0:
                A[i] = self._tau[i] / 6.

        C[:-1] = np.copy(A[1:])

        for i in range(1, N - 1):
            mult = A[i] / B[i - 1]
            B[i] = B[i] - mult * C[i - 1]
            D[i] = D[i] - mult * D[i - 1]

        self._m[N - 1] =  D[N - 2] / B[N - 2]
        for i in range(N - 3, -1, -1):  # zero exclusive, N - 2 iterations exactly
            self._m[i + 1] = (D[i] - C[i] * self._m[i + 2]) / B[i]

        for i in range(N):
            self._a[i] = f[i] / self._tau[i] - self._m[i] * self._tau[i] / 6.
            self._b[i] = f[i + 1] / self._tau[i] - self._m[i + 1] * self._tau[i] / 6.

    def _find_segment(self, x: float):
        """
            x: float point to be interpolated

            returns: index of segment in grid (0 if x < x_min, N - 1 if x > x_max)
        """

        left = 0
        right = len(self._tau)  # max ind + 1

        while right - left > 1:
            mid = (right + left) // 2
            if x < self._grid[mid][0]:
                right = mid
            else:
                left = mid

        return left

    def _interpolate(self, x: float):
        n = self._find_segment(x)

        x_n0 = self._grid[n][0]
        if n >= len(self._tau) or abs(x - x_n0) < 1e-6:
            return self._grid[n][1]

        x_n1 = self._grid[n + 1][0]

        return 1. / (6. * self._tau[n]) * (
            self._m[n] * pow(x_n1 - x, 3.) +
            self._m[n + 1] * pow(x - x_n0, 3.)
        ) + self._a[n] * (x_n1 - x) + self._b[n] * (x - x_n0)

    def __call__(self, x: float):
        if self._tau is None:
            self._calc_coefs()

        return self._interpolate(x)


if __name__ == '__main__':
    f = SplineInterpolation([
        (2., 4.),
        (3., 9.),
        (-2., 4.),
        (-1., 1.),
        (1., 1.),
        (4., 16.),
    ])

    print(f(2.))
    print(f(3))
    print(f(3.))
    print(f.dump_to_dict())