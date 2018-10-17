class ParamFunc(object):

    def __init__(self, paramsDict):
        self.params = paramsDict

    def __call__(self):
        pass

    def tabulate(self, beg, end):
        results = []
        for x in range(beg, end):
            results.append(self(x))

class PlanFunc(ParamFunc):

    def __call__(self):
        pass