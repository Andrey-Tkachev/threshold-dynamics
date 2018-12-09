import numpy as np
from functools import partial

class Integral(object):
    _prec = None

    def __init__(self, func, nodes_num: int = 1000):
        """
        :param func: function to inetegrate with overloaded operator()
        :param step: step of the partition
        :param method: integration method one of 'trap', 'simps'
        """

        self.func = func
        self.nodes_num = nodes_num

    @classmethod
    def error(cls, func, begin, end, nodes_num):
        hig = cls(func, nodes_num)
        low = cls(func, nodes_num // 2)
        return abs(hig(begin, end) - low(begin, end)) / (2. ** float(cls._prec) - 1.)

    def _proc(self, begin, end, grid):
        raise NotImplemented

    def __call__(self, begin: float, end: float = 1.0,  grid = None) -> float:
        """
        :param end: integrate func from ? to end.
        :param begin: integrate func from begin to end.

        :return integral from begin to end
        """
        if grid is None:
            grid = np.linspace(begin, end, num=self.nodes_num, endpoint=True)

        return self._proc(begin, end, grid)

class TrapzIntegral(Integral):
    _prec = 3

    def _proc(self, begin, end, grid):
        accum = 0.0
        for i, x in enumerate(grid[:-1]):
            y = self.func(x)
            next_y = self.func(grid[i + 1])
            accum += (y + next_y) * (grid[i + 1] - grid[i]) / 2.0

        return accum


class SimpsIntegral(Integral):
    _prec = 5

    def _proc(self, begin, end, grid):
        accum = 0.0
        h = (end - begin) / self.nodes_num
        for i, x in enumerate(grid[:-1]):
            y_0 = self.func(x)
            y_05 = self.func(x + 0.5 * h)
            y_1 = self.func(x + h)
            accum += (y_0 + y_1 + 4.0 * y_05)

        return accum * h / 6.


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import scipy.integrate as integrate
    import scipy.special as special
    from numpy import sqrt, sin, cos, pi

    plain_func = lambda x: special.jv(2.5, x) + sin(x / 10)
    gap_func = lambda x: x ** 0.5 if x < 4. else x ** 0.4 - 2.
    osc_func = lambda x: sin(x ** 0.1) * 10 - 1

    beg = 0
    end = 15

    funcs = [(gap_func, 'Gap'), (osc_func, 'Osc'), (plain_func, 'Plain')]

    for func, name in funcs:
        res = integrate.quad(func, beg, end)[0]
        print(f'Framework method result is {res:.4f}')
        for method in [SimpsIntegral, TrapzIntegral]:
            my_res = method(func, nodes_num=20000)(end, begin=beg)
            print(method.__name__, 'of', name, f'function is {my_res:.4f}')

    raise BaseException
    def mk_plot(func, rng, label, same=False):
        plt.plot(rng, [func(x) for x in rng], label=label)
        plt.grid(True)
        plt.legend()
        if not same:
            plt.show()

    def self_error(nodes_num, method, func=None):
        return method.error(func, beg, end, nodes_num)

    def error_compare(nodes_num, method, func=None):
        etalon, err = integrate.quad(func, beg, end)
        integr = method(func, nodes_num=nodes_num)
        my_val = integr(begin=beg, end=end)

        return abs(my_val - etalon)

    for func, name in [(gap_func, 'Gap'), (osc_func, 'Osc'), (plain_func, 'Plain')]:
        rng = np.arange(1000, 40000, 5000)
        for method in [SimpsIntegral]:  # , TrapzIntegral]:
            plt.title('Self error')
            mk_plot(
                partial(self_error, func=func, method=method),
                rng,
                name + ' ' + method.__name__,
                same=True
            )

            plt.xlabel('N')
            plt.ylabel('Runge rule')
            plt.show()

    plt.title('Compare error')
    for func, name in [(osc_func, 'Osc')]:
        rng = np.arange(100, 50000, 1000)
        for method in [SimpsIntegral, TrapzIntegral]:
            mk_plot(
                partial(error_compare, func=func, method=method),
                rng,
                name + ' ' + method.__name__,
                same=True
            )

    plt.xlabel('log(N)')
    plt.ylabel('log(error)')
    plt.yscale('log')
    plt.xscale('log')
    plt.show()