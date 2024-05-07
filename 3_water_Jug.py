class WaterJugProblem:
    def __init__(self, jug1_capacity, jug2_capacity, target):
        self.jug1_capacity = jug1_capacity
        self.jug2_capacity = jug2_capacity
        self.target = target
        self.states = set()

    def pour(self, jug1, jug2):
        if (jug1, jug2) in self.states:
            return False
        self.states.add((jug1, jug2))
        if jug1 == self.target or jug2 == self.target:
            return True
        if self.pour(jug1, self.jug2_capacity): return True
        if self.pour(self.jug1_capacity, jug2): return True
        if self.pour(0, jug2): return True
        if self.pour(jug1, 0): return True
        transfer = min(jug1, self.jug2_capacity - jug2)
        if self.pour(jug1 - transfer, jug2 + transfer): return True
        transfer = min(self.jug1_capacity - jug1, jug2)
        if self.pour(jug1 + transfer, jug2 - transfer): return True
        return False

    def solve(self):
        if self.pour(0, 0):
            print("Solution found!")
        else:
            print("No solution found!")


# Example usage
jug1_capacity = 4
jug2_capacity = 3
target = 3
problem = WaterJugProblem(jug1_capacity, jug2_capacity, target)
problem.solve()
