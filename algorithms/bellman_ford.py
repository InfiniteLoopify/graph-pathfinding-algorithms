import sys
from main import printLine


class BellmanFord:
    SPT = []
    distance = []
    prev = []

    def runAlgorithm(self, graph, V, node):
        self.SPT = []
        self.distance = []
        self.prev = []

        self.distance = [sys.maxsize] * V
        self.prev = [None] * V
        self.distance[node] = 0
        for i in range(V):
            for j in range(V):
                if graph[i][j] != 0:
                    tempDistance = self.distance[i] + graph[i][j]
                    if tempDistance < self.distance[j]:
                        self.distance[j] = tempDistance
                        self.prev[j] = i

        for i in range(V):
            if self.prev[i] == None:
                self.SPT.append([i, i])
            else:
                self.SPT.append([i, self.prev[i]])

        # print algo info
        self.costSum()
        self.printAlgo(node)

        return self.SPT

    def printAlgo(self, node):
        printLine()
        print("Cost from Starting Node:")
        for i in range(len(self.distance)):
            print("(", node, "->", i, ") :\t", self.distance[i])

    def costSum(self):
        sum = 0
        for i in self.distance:
            sum += i
        printLine()
        print("Total Cost: ", sum)
