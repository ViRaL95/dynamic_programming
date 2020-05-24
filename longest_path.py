from typing import List

def find_longest_path(N, edges:List[List[int]]):
    adjacency_list, indegree = build_adjacency_list_indegree(N, edges)
    print(adjacency_list, indegree)
    visited = set()
    distance_map = {vertice: 0 for vertice in range(1, N + 1)}

    for vertice in range(1, N + 1):
        if vertice not in visited and indegree[vertice - 1] == 0:
            dfs(vertice, adjacency_list, indegree, visited,  distance_map)

    print(distance_map)
    return max(distance_map.values())


def dfs(current_vertice, adjacency_list, indegree, visited, distance_map):
    if current_vertice in visited:
        return

    visited.add(current_vertice)

    print(f"current vertice is {current_vertice}")
    for adjacent_vertice in adjacency_list[current_vertice]:
        indegree[adjacent_vertice - 1] -= 1
        distance_map[adjacent_vertice] = max(distance_map[adjacent_vertice], distance_map[current_vertice] + 1)
        if indegree[adjacent_vertice - 1] == 0:
            dfs(adjacent_vertice, adjacency_list, indegree, visited, distance_map)



def build_adjacency_list_indegree(N, edges):
    adjacency_list = {}
    indegree = [0] * N
    print(indegree)
    for source, destination in edges:
        if source not in adjacency_list:
            adjacency_list[source] = [destination]
        else:
            adjacency_list[source].append(destination)

        if destination not in adjacency_list:
            adjacency_list[destination] = []

        indegree[destination - 1] += 1

    return adjacency_list, indegree


if __name__ == '__main__':
    print(find_longest_path(4, [[1, 2], [1, 3], [3, 2], [2, 4], [3, 4]]))