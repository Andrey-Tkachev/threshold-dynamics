import utils
import numpy as np

if __name__ == '__main__':
    plan = lambda t: 1 - (1 - t) ** 2 +  np.sin(t)
    z = lambda t: 2 * t ** 0.5
    p = lambda w: 6. * w * (1. - w)

    utils.dumpFunc(plan, './test_data/plan.csv', mode=None, rng=(0, 1, 0.01))
    utils.dumpFunc(z, './test_data/z.csv', mode=None, rng=(0, 1, 0.01))
    utils.dumpFunc(p, './test_data/p.csv', mode=None, rng=(0, 1, 0.01))