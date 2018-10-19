import numpy as np

class Interpolation(object):

    def __init__(self, points=[], name='id'):
        self.coefs = []
        self._interpolate(points)
        self.name = name

    def _interpolate(self, points):
        self._points = sorted(points)
        self._coefs = np.random.rand(len(points))

    def __call__(self, x):  # mock interpolation
        if len(self._points) < 2:
            return x

        left = 0
        right = len(self._points) - 1
        while right - left > 1:
            mid = (right + left) // 2
            if x < self._points[mid][0]:
                right = mid
            else:
                left = mid
        p_left, p_right = self._points[left], self._points[left + 1]

        lx, ly = p_left
        rx, ry = p_right
        return ly + (ry - ly) * (x - lx) / (rx - lx)

    def getCoefs(self):
        return self._coefs

    def setCoefs(self, coefs):
        self._coefs = coefs
        return self

if __name__ == '__main__':
    f = Interpolation([(1, 1.), (2, 2.), (3, 1.)])
    print(f(2.5))
    print(f.getCoefs())