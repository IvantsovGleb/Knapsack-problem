import unittest
from ortools.algorithms import pywrapknapsack_solver
unittest.TestLoader.sortTestMethodsUsing = None


class ParametrizedTestKnapsack(unittest.TestCase):
    def __init__(self, methodName='runTest', param=None):
        super(ParametrizedTestKnapsack, self).__init__(methodName)
        self.knapsack = param

    @staticmethod
    def parametrize(testcase_klass, param=None):
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_klass(name, param=param))
        return suite


class Test(ParametrizedTestKnapsack):
    def knapsack_solver(self, p, w, cap):
        solver = pywrapknapsack_solver.KnapsackSolver(
            pywrapknapsack_solver.KnapsackSolver.
                KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER, 'Knapsack')
        solver.Init(p, w, cap)
        computed_value = solver.Solve()
        packed_items = []
        packed_weights = []
        for i in range(len(p)):
            if solver.BestSolutionContains(i):
                packed_items.append(i)
                packed_weights.append(w[0][i])
        return packed_items, packed_weights, computed_value

    def test(self):
        actual = self.knapsack.solver()
        expected = self.knapsack_solver(self.knapsack.profits,
                                        [self.knapsack.weights],
                                        [self.knapsack.capacity])
        for one, two in zip(actual, expected):
            self.assertEqual(one, two)
