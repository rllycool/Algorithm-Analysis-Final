import math
def tsp(cities):
    num_cities = len(cities)
    visited = [False] * num_cities
    tour = []

    current_city = 0
    visited[current_city] = True
    tour.append('A')

    # find the nearest neighboring city
    for _ in range(num_cities - 1):
        nearest_neighbor = None
        min_distance = math.inf

        # find the nearest unvisited city
        for i in range(num_cities):
            if not visited[i]:
                distance = calculate_distance(cities[current_city], cities[i])
                if distance < min_distance:
                    min_distance = distance
                    nearest_neighbor = i

        # visit the nearest neighbor
        visited[nearest_neighbor] = True
        tour.append(citylist[nearest_neighbor])
        current_city = nearest_neighbor

    return tour

#helper method to find distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

citylist = ['A', 'B', 'C', 'D', 'E', 'F']
cities = [(0, 0), (3, 4), (5, 5), (4, 1), (1, 2), (1, 5)]
tour = tsp(cities)
print(tour)

