import sys


class Prims:
    MST = []
    visited = []

    def minKey(self, key, mstSet, V):
        min = sys.maxsize
        for v in range(V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
        return min_index

    def runAlgorithm(self, graph, V, node):
        self.MST = []
        key = [sys.maxsize] * V
        parent = [None] * V
        key[0] = 0
        self.visited = [False] * V
        parent[0] = -1

        for cout in range(V):
            u = self.minKey(key, self.visited, V)
            self.visited[u] = True
            for v in range(V):
                if graph[u][v] > 0 and self.visited[v] == False and key[v] > graph[u][v]:
                    key[v] = graph[u][v]
                    parent[v] = u

        for i in range(1, V):
            self.MST.append([parent[i], i])
        return self.MST
