import numpy as np

class TSPSolver:
    def __init__(self, distances):
        self.distances = distances
        self.num_cities = len(distances)
        self.visited = np.zeros(self.num_cities, dtype=bool)

    def nearest_neighbor(self, start_city):
        route = [start_city]
        self.visited[start_city] = True

        while len(route) < self.num_cities:
            current_city = route[-1]
            nearest_city = None
            min_distance = float('inf')

            for city in range(self.num_cities):
                if not self.visited[city] and self.distances[current_city][city] < min_distance:
                    nearest_city = city
                    min_distance = self.distances[current_city][city]

            route.append(nearest_city)
            self.visited[nearest_city] = True

        return route

    def total_distance(self, route):
        total = 0
        for i in range(len(route)):
            total += self.distances[route[i-1]][route[i]]
        return total

# Example usage
distances = np.array([[0, 10, 15, 20],
                      [10, 0, 35, 25],
                      [15, 35, 0, 30],
                      [20, 25, 30, 0]])

tsp_solver = TSPSolver(distances)
route = tsp_solver.nearest_neighbor(0)
print("Optimal route:", route)
print("Measured distance:", tsp_solver.total_distance(route))
