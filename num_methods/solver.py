import numpy as np

from .interpolation import Interpolation

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
        return Interpolation(np.random.rand((10, 2)))

    def getBetta(self):
        return 42

    def getC1(self):
        return 2.4

    def getC2(self):
        return 1.8