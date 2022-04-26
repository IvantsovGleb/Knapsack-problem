class Knapsack:
    def __init__(self):
        self.profits = []
        self.weights = []
        self.number = 0
        self.capacity = 0

    def solver(self):
        A = [0 for i in range(self.capacity + 1)]
        B = [[0 for i in range(self.capacity + 1)] for j in range(self.number)]
        for k in range(self.number):
            for y in reversed(range(self.capacity + 1)):
                if self.weights[k] <= y \
                        and A[y] < A[y - self.weights[k]] + self.profits[k]:
                    A[y] = A[y - self.weights[k]] + self.profits[k]
                    B[k][y] = 1
                else:
                    B[k][y] = 0

        packed_items = []
        y = self.capacity
        for k in reversed(range(self.number)):
            if B[k][y] == 1:
                packed_items.append(k)
                y = y - self.weights[k]

        computed_value = 0
        packed_weights = []
        for k in packed_items:
            computed_value += self.profits[k]
            packed_weights.append(self.weights[k])

        return packed_items[::-1], packed_weights[::-1], computed_value
