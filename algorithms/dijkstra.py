import sys
from main import printLine


class Dijkstra:
    SPT = []
    visited = []
    cost = []

    def runAlgorithm(self, graph, V, node):
        self.SPT = []
        self.visited = []
        self.cost = []
        nodeInit = node

        for i in range(0, V):
            self.cost.append([sys.maxsize, -1])

        self.cost[node] = [0, -1]
        while len(self.visited) != V:
            self.visited.append(node)
            for j in range(0, V):
                if (graph[node][j] != 0) and not (j in self.visited) and (self.cost[node][0] + graph[node][j] <= self.cost[j][0]):
                    self.cost[j][0] = self.cost[node][0] + graph[node][j]
                    self.cost[j][1] = node

            nextMin = [0, sys.maxsize]
            for j in range(len(self.cost)):
                if (self.cost[j][0] < nextMin[1]) and (j not in self.visited):
                    nextMin = [j, self.cost[j][0]]

            node = nextMin[0]

        for i in range(0, len(self.cost)):
            if self.cost[i][1] == -1:
                self.SPT.append([i, i])
            else:
                self.SPT.append([i, self.cost[i][1]])

        # print algo info
        self.costSum()
        self.printAlgo(nodeInit)

        return self.SPT

    def printAlgo(self, node):
        printLine()
        print("Cost from Starting Node:")
        for i in range(len(self.cost)):
            print("(", node, "->", i, ") :\t", self.cost[i][0])

    def costSum(self):
        sum = 0
        for i in self.cost:
            sum += i[0]
        printLine()
        print("Total Cost: ", sum)
