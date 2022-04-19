import os
import unittest
from knapsack_tests import ParametrizedTestKnapsack, Test
from knapsack import Knapsack

if __name__ == '__main__':
    suite = unittest.TestSuite()
    filenames = next(os.walk("./datasets"))[2]
    for i in range(1, int(len(filenames) / 3) + 1):
        knapsack = Knapsack()
        with open('datasets/p0' + str(i) + '_p.txt', 'r') as f:
            knapsack.profits = [int(profit) for profit in f]
        with open('datasets/p0' + str(i) + '_w.txt', 'r') as f:
            knapsack.weights = [int(weight) for weight in f]
        with open('datasets/p0' + str(i) + '_c.txt', 'r') as f:
            knapsack.capacity = int(f.read())
        knapsack.number = len(knapsack.profits)
        suite.addTest(ParametrizedTestKnapsack.parametrize(Test, knapsack))
    unittest.TextTestRunner(verbosity=2).run(suite)
