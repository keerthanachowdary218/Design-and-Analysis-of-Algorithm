# -*- coding: utf-8 -*-
"""IsGoodGraohOrNot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vBegcblHyvce9FjMcahWb9gJ5QVu9YBO
"""

def is_good_graph(graph):
    n = len(graph)  # Number of vertices
    V1, V2 = set(), set()  # Initialize sets V1 and V2
    colors = [-1] * n  # -1 indicates unassigned

    def dfs(vertex, color):
        nonlocal V1, V2, colors

        # Assign color to the current vertex
        colors[vertex] = color

        # Add vertex to the corresponding set
        if color == 0:
            V1.add(vertex)
        else:
            V2.add(vertex)

        # Explore neighbors
        for neighbor in graph[vertex]:
            if colors[neighbor] == -1:
                # Neighbor is not colored, assign the opposite color
                if not dfs(neighbor, 1 - color):
                    return False
            elif colors[neighbor] == color:
                # Neighbor has the same color, not a "good" graph
                return False

        return True

    # Start DFS from an arbitrary vertex
    for vertex in range(n):
        if colors[vertex] == -1:
            if not dfs(vertex, 0):
                return False

    # Check if all edges are crossing edges
    for vertex in range(n):
        for neighbor in graph[vertex]:
            if colors[vertex] == colors[neighbor]:
                return False

    # The graph is "good"
    return True

graph = {
    0: [1],
    1: [2],
    2: [3, 0],
    3: [0]
}

result = is_good_graph(graph)
print(result)