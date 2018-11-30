import numpy as np

from .interpolation import SplineInterpolation

class Solver(object):

    def __init__(self, x0, y0, betta, t, u, s, z):
        self.x0 = x0
        self.y0 = y0
        self.betta = betta
        self.t = t
        self.u = u
        self.s = s
        self.z = z

    def solve(self):
        grid = []
        for x in np.arange(0, 10):
            grid.append((x, self.u(x) / (self.z(x) + 10.) + self.s(x - 1.)))
        return SplineInterpolation(grid=grid)

    def getBetta(self):
        return 42

    def getC1(self):
        return 2.4

    def getC2(self):
        return 1.8