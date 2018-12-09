import numpy as np
import utils

class CorrectionFunction(object):

    def __init__(self, betta):
        self.betta = betta

    def __call__(self, z, x, S):
        return (x - S) * self.betta + (-(z - S) ** self.betta) ** (x < S)

class LossFunction(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, c1, c2):
        return c1 * self.a + c2 * self.b