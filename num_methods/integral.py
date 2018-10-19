class Integral(object):

    def __init__(self, func):
        self.func = func

    def __call__(self, t):
        return t * (self.func(t) + self.func(0.)) / 2.