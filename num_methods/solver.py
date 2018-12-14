import numpy as np

from .interpolation import SplineInterpolation
from .integral import TrapzIntegral
from control_functions import CorrectionFunction, LossFunction

def derevative(f, x, h=0.001):
    return (-f(x + 2 * h) + 8. * f(x + h) - 8. * f(x - h) + f(x - 2 * h)) / (12. * h)

class CauchySolver(object):

    def __init__(self, functions):
        """
            functions: array of callable objects, where functions[i] = func[t, x_1, x_2 ... x_n], n = |funcs|
        """

        self._f = functions

    def solve(self, init_valuess, T: float, h=0.0001, constrains=None):
        """
            init_values: array of init values, |funcs| = |init_values|
            h: step of the method
            constraints: n-len array of none or tuples with constraints

            returns: nodes, array |funcs| x |T / h|, grid of result funcs by rows in nodes h * row_ind
        """
        iv = np.array(init_valuess)
        answer_values = iv
        ts = np.arange(0, T + h / 2., h)

        for t in ts[1:]:
            k1 = h * np.array([
                func(t, *iv) for func in self._f
            ])

            k2 = h * np.array([
                func(t + h / 2., *(iv + k1 / 2.)) for func in self._f
            ])

            k3 = h * np.array([
                func(t + h / 2., *(iv + k2 / 2.)) for func in self._f
            ])

            k4 = h * np.array([
                func(t + h, *(iv + k3)) for func in self._f
            ])

            iv = iv + 1 / 6. * (k1 + 2. * k2 + 2. * k3 + k4)
            if constrains is not None:
                for i in range(len(iv)):
                    if constrains[i] is not None:
                        iv[i] = min(max(iv[i], constrains[i][0]), constrains[i][1])

            answer_values = np.vstack((answer_values, iv))

        return ts, [row.flatten() for row in answer_values.T]

class Solver(object):

    def __init__(self, x0, y0, betta, t, u, s, z, p,
                            auto=False,
                            c1_weight=1.,
                            c2_weight=1.,
                            progress_callback=None):
        self.x0 = x0 if not auto else s(0)
        self.y0 = y0
        self.betta = betta
        self.t = t
        self.u = u
        self.s = s
        self.z = z
        self.p = p
        self.auto = auto
        self.progress_callback = progress_callback
        self.loss_func = LossFunction(c1_weight, c2_weight)

    def log(self, message):
        if self.progress_callback is not None:
            self.progress_callback(message)
        else:
            print(message)

    def _solve_with_betta(self, betta):
        f_betta = CorrectionFunction(betta)
        funcs = [
            lambda t, x, y: derevative(self.z, t) * self.u(y),
            lambda t, x, y: f_betta(self.z(t), x, self.s(t))
        ]

        initials = [self.x0, self.y0]

        if not self.auto:
            self.log('Solving Cauchy')
        cauchy = CauchySolver(funcs)
        grid, solutions = cauchy.solve(initials, self.t, constrains=[None, (0, 1)])

        if not self.auto:
            self.log('Interpolate results')
        real_shows = SplineInterpolation([pair for pair in zip(grid, solutions[0])])
        threshold = SplineInterpolation([pair for pair in zip(grid, solutions[1])])
        return real_shows, threshold

    def solve(self):
        if self.auto:
            self.log('Solving in auto mode')
            betta0, betta1 = self.betta
            best_loss = None
            betta_opt = None
            c1_on_opt = None
            c2_on_opt = None

            betta_array = np.linspace(betta0, betta1, 20)
            losses = []

            best_solution = None
            for betta in betta_array:
                self.log(f'Testing betta {betta:.2f}')
                real_shows, threshold = self._solve_with_betta(betta)
                c1 = self.getC1(real_shows, threshold, self.x0)
                c2 = self.getC2(real_shows)
                loss = self.loss_func(c1, c2)
                if best_loss is None or loss < best_loss:
                    best_loss = loss
                    betta_opt = betta
                    c1_on_opt = c1
                    c2_on_opt = c2
                    best_solution = (real_shows, threshold)
                self.log(f'C1 {c1:.2f}\nC2 {c2:.2f}\nLoss {loss:.2f}')
                losses.append(loss)

            self.log('Interpolating loss')
            loss_func = SplineInterpolation(list(zip(betta_array, losses)))
            return (
                best_solution[0],
                best_solution[1],
                betta_opt,
                c1_on_opt,
                c2_on_opt,
                loss_func
            )
        else:
            real_shows, threshold = self._solve_with_betta(self.betta)
            return (
                real_shows,
                threshold,
                self.getC1(real_shows, threshold, self.x0),
                self.getC2(real_shows),
            )

    def getC1(self, real_shows, threshold, x0):
        if not self.auto:
            self.log('Calculating C1')
        wpw = TrapzIntegral(lambda t: threshold(t) * t, nodes_num=100)
        functional = lambda t: derevative(real_shows, t) * wpw(t)
        functional_value = TrapzIntegral(functional, nodes_num=1000)(0.0, self.t)
        return 1. - functional_value / (real_shows(self.t) - x0)

    def getC2(self, real_shows):
        if not self.auto:
            self.log('Calculating C2')
        return abs(real_shows(self.t) - self.s(self.t)) / self.s(self.t)
