import sys
from main import printLine


class Floyd:
    SPT = []
    cost = []
    last = []

    def runAlgorithm(self, graph, V, node):

        self.SPT = []
        self.cost = []

        self.last = [[-1 for i in range(V)]
                     for j in range(V)]

        self.cost = [[0 for i in range(V)] for j in range(V)]
        for i in range(V):
            for j in range(V):
                if i == j:
                    self.cost[i][j] = 0
                elif graph[i][j] != 0:
                    self.cost[i][j] = graph[i][j]
                    self.last[i][j] = j
                else:
                    self.cost[i][j] = sys.maxsize

        for k in range(V):
            for i in range(V):
                for j in range(V):
                    if self.cost[i][j] > self.cost[i][k] + self.cost[k][j]:
                        self.cost[i][j] = self.cost[i][k] + self.cost[k][j]
                        self.last[i][j] = self.last[i][k]

        for i in range(V):
            for j in range(V):
                if not (i == j or self.cost[i][j] == sys.maxsize) and i == node:
                    path = [i]
                    while path[-1] != j:
                        path.append(self.last[path[-1]][j])

                    for k in range(0, len(path) - 1):
                        if not ([path[k], path[k+1]] in self.SPT or [path[k+1], path[k]] in self.SPT):
                            self.SPT.append([path[k], path[k+1]])
                    """ print("%d → %d  %4d       %s"
                          % (i + 1, j + 1, self.cost[i][j],
                             ' → '.join(str(p) for p in path))) """

        # print algo info
        self.costSum(V, node)
        self.printAlgo(node)

        return self.SPT

    def printAlgo(self, node):
        printLine()
        print("Cost from Starting Node:")
        for i in range(len(self.cost)):
            print("(", node, "->", i, ") :\t", self.cost[node][i])

    def costSum(self, V, node):
        sum = 0
        for i in range(V):
            sum += self.cost[node][i]
        printLine()
        print("Total Cost: ", sum)
