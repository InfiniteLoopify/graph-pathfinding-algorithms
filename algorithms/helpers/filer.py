class File:
    nodesCordinate = []
    graph = []
    nodesCount = 0
    fileX = None
    maxXY = [0.0, 0.0]
    startNode = 0

    def __init__(self, fileName):
        self.fileX = open(fileName, "r")
        if self.fileX.mode != "r":
            print("File unable to read")

    def readLinesN(self, times):
        if self.fileX is None:
            return

        for i in range(times):
            self.fileX.readline()

    def readNodeCount(self):
        if self.fileX is None:
            return

        self.readLinesN(2)
        self.nodesCount = int(self.fileX.readline())
        self.graph = [
            [0 for i in range(self.nodesCount)] for j in range(self.nodesCount)
        ]

    def readNodesCordinate(self):
        if self.fileX is None:
            return

        self.readLinesN(1)
        for i in range(self.nodesCount):
            line = self.fileX.readline()
            fields = line.split("\t")
            self.nodesCordinate.append([float(fields[1]), float(fields[2])])
            self.maxXY[0] = (
                float(fields[1]) if float(fields[1]) > self.maxXY[0] else self.maxXY[0]
            )
            self.maxXY[1] = (
                float(fields[2]) if float(fields[2]) > self.maxXY[1] else self.maxXY[1]
            )

    def readGraph(self):
        if self.fileX is None:
            return

        self.readLinesN(1)
        for i in range(self.nodesCount):
            line = self.fileX.readline()
            fields = line.split("\t")
            fromNode = int(fields[0])
            for j in range(1, len(fields) - 1, 4):
                toNode = int(fields[j])
                cost = float(fields[j + 2]) / (10**7)
                if toNode == fromNode:
                    self.graph[toNode][fromNode] = 0
                elif (
                    self.graph[toNode][fromNode] == 0
                    or cost < self.graph[toNode][fromNode]
                ):
                    self.graph[toNode][fromNode] = cost
                    self.graph[fromNode][toNode] = cost
                else:
                    self.graph[fromNode][toNode] = self.graph[toNode][fromNode]

    def readStartNode(self):
        if self.fileX is None:
            return

        self.readLinesN(1)
        self.startNode = int(self.fileX.readline())

    def readFile(self):
        self.nodesCordinate = []
        self.graph = []
        self.nodesCount = 0
        self.maxXY = [0.0, 0.0]
        self.startNode = 0

        self.readNodeCount()
        self.readNodesCordinate()
        self.readGraph()
        self.readStartNode()

    def __del__(self):
        if self.fileX is None:
            return
        self.fileX.close()
