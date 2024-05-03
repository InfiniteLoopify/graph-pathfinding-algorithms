class Kruskal:
    MST = []
    sortedEdge = []
    traverseStack = []
    X = False

    def sorter(self, elem):
        return elem[2]

    def sortAllEdges(self, graph, V):
        for i in range(0, V):
            for j in range(i + 1, V):
                if graph[i][j] != 0:
                    self.sortedEdge.append([i, j, graph[i][j]])
        self.sortedEdge.sort(key=self.sorter, reverse=True)

    def traverseCycle(self, V, start, end):

        if start == end or self.X:
            self.X = True
            return self.X

        for i in range(0, V):
            if ([start, i] in self.MST or [i, start] in self.MST) and not ([start, i] in self.traverseStack or [i, start] in self.traverseStack):
                self.traverseStack.append([start, i])
                self.traverseCycle(V, i, end)

    def runAlgorithm(self, graph, V, node):
        self.MST = []
        self.sortedEdge = []

        self.sortAllEdges(graph, V)

        while (len(self.MST) != V - 1) and self.sortedEdge:
            temp = self.sortedEdge.pop()
            self.traverseStack = []
            self.X = False
            self.traverseCycle(V, temp[0], temp[1])

            if not self.X:
                self.MST.append([temp[0], temp[1]])

        return self.MST
