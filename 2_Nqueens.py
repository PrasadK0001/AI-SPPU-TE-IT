import random

class NQueens:
    def __init__(self, N):
        self.N = N
        self.board = self.initial_state()

    def initial_state(self):
        return [random.randint(0, self.N-1) for _ in range(self.N)]

    def attack_pairs(self, state):
        attacks = 0
        for i in range(len(state)):
            for j in range(i+1, len(state)):
                if state[i] == state[j] or abs(state[i]-state[j]) == abs(i-j):
                    attacks += 1
        return attacks

    def heuristic(self, state):
        return -self.attack_pairs(state)

    def get_neighbors(self, state):
        neighbors = []
        for i in range(len(state)):
            for j in range(self.N):
                if j != state[i]:
                    neighbor = list(state)
                    neighbor[i] = j
                    neighbors.append(neighbor)
        return neighbors

    def hill_climbing(self):
        current_state = self.board
        current_heuristic = self.heuristic(current_state)

        while True:
            neighbors = self.get_neighbors(current_state)
            best_neighbor = None
            best_heuristic = current_heuristic

            for neighbor in neighbors:
                neighbor_heuristic = self.heuristic(neighbor)
                if neighbor_heuristic > best_heuristic:
                    best_neighbor = neighbor
                    best_heuristic = neighbor_heuristic

            if best_heuristic <= current_heuristic:
                return current_state

            current_state = best_neighbor
            current_heuristic = best_heuristic

    def print_board(self, state):
        for row in range(self.N):
            line = ""
            for col in range(self.N):
                if state[col] == row:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print()

if __name__ == "__main__":
    N = 8  # Change N for different board sizes
    queens = NQueens(N)
    solution = queens.hill_climbing()
    print("Solution:")
    queens.print_board(solution)
