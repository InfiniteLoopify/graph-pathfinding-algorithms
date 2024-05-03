import networkx as nx
import matplotlib.pyplot as plt

from algorithms.helpers.file_handler import File
from algorithms.helpers.gui import Gui


def printLine():
    print("-----------------------------------")


def importAlgo(algoChoose):
    algoList = ["Prims", "Kruskal", "Dijkstra", "Bellman Ford", "Floyd"]
    algoObj = None
    printLine()
    print("Algo Used: ", algoList[algoChoose])
    if algoChoose == 0:
        from algorithms import prims as algo

        algoObj = algo.Prims()
    elif algoChoose == 1:
        from algorithms import kruskal as algo

        algoObj = algo.Kruskal()
    elif algoChoose == 2:
        from algorithms import dijkstra as algo

        algoObj = algo.Dijkstra()
    elif algoChoose == 3:
        from algorithms import bellman_ford as algo

        algoObj = algo.BellmanFord()
    elif algoChoose == 4:
        from algorithms import floyd as algo

        algoObj = algo.Floyd()
    else:
        print("invalid Module index passed")
        return False
    return algoObj


def operateHex(color, val):
    color = (hex(int(color, base=16) + val))[2:]
    color = ("0" if len(color) <= 1 else "") + color
    color = ("0" if len(color) <= 1 else "") + color
    return color


def addEdges(graph, fileObj, selectedPath, showAllEdges):

    edge_width = []
    default_width = 0.4
    redColor = "#ff0000"
    color = ["00", "ff"]
    changeStep = int(255 / ((fileObj.nodesCount**2) / 2))
    if not changeStep:
        changeStep = 1

    for i in range(len(fileObj.graph)):
        for j in range(i + 1, len(fileObj.graph)):

            if [i, j] in selectedPath or [j, i] in selectedPath:
                edge_width.append(default_width * 1.5)
                graph.add_edge(i, j, weight=fileObj.graph[i][j], color=redColor)

            elif fileObj.graph[i][j] != 0 and showAllEdges:
                tempColor = "#%s%s%s%s" % (color[0], color[0], color[0], color[1])
                edge_width.append(default_width)
                graph.add_edge(i, j, weight=fileObj.graph[i][j], color=tempColor)

                if not (color[0] == "80" or color[1] == "80"):
                    color[0] = operateHex(color[0], changeStep)
                    color[1] = operateHex(color[1], -changeStep)
    return edge_width


def addNodes(G, fileObj):

    node_edge_color = []
    node_edge_width = []
    for i in range(fileObj.nodesCount):
        if i == fileObj.startNode:
            node_edge_color.append("#000044")
            node_edge_width.append(1.2)
        else:
            node_edge_color.append("#5555ff")
            node_edge_width.append(0.8)
        G.add_node(i, pos=(fileObj.nodesCordinate[i][0], fileObj.nodesCordinate[i][1]))
    return node_edge_color, node_edge_width


def clusterCoefficient(fileObj):

    lccFinal = 0.0
    for i in range(fileObj.nodesCount):
        degree = 0
        link = 0
        visited = []

        for j in range(fileObj.nodesCount):
            if fileObj.graph[i][j] != 0:
                degree += 1
                visited.append(j)
        for j in visited:
            for k in range(fileObj.nodesCount):
                if fileObj.graph[j][k] != 0 and k in visited:
                    link += 1
            visited.remove(j)

        maxLink = (degree * (degree - 1)) / 2
        if maxLink == 0:
            maxLink = 1
        lcc = link / maxLink
        lccFinal += lcc

    lccFinal /= fileObj.nodesCount
    return lccFinal


def calculateCost(edgeList, graph, V):
    totalCost = 0
    for edge in edgeList:
        totalCost += graph[edge[0]][edge[1]]
    return totalCost


def main():
    # graphing variables
    fileName = "files/input100.txt"
    algoIndex = 4
    showAllEdges = False
    showWeights = True

    # create user input gui
    gui = Gui()
    gui.guiCreate()
    fileName = "files/" + gui.guiArray[0]
    algoIndex = gui.guiArray[1]
    showAllEdges = gui.guiArray[2]
    showWeights = gui.guiArray[3]

    # read input file
    fileObj = File(fileName)
    fileObj.readFile()

    # apply algo
    algoObj = importAlgo(algoIndex)
    selectedPath = algoObj.runAlgorithm(
        fileObj.graph, fileObj.nodesCount, fileObj.startNode
    )

    # print selected path
    printLine()
    print("Selected Edges:")
    for pathI, pathJ in selectedPath:
        print("(", pathI, "->", pathJ, ") :\t", fileObj.graph[pathI][pathJ])
    # print(selectedPath)

    printLine()
    print(
        "Total Edge Cost: %0.2f"
        % calculateCost(selectedPath, fileObj.graph, fileObj.nodesCount)
    )

    # display local clustering coefficient
    localClusterVal = clusterCoefficient(fileObj)
    printLine()
    print("Clustering Coefficient: %0.2f" % localClusterVal)

    # plot axis
    fig, ax = plt.subplots()
    fig.add_subplot(111)
    ax.axis((0, fileObj.maxXY[0], 0, fileObj.maxXY[1]))

    # add nodes and edges
    G = nx.Graph()
    node_edge_color, node_edge_width = addNodes(G, fileObj)
    edge_width = addEdges(G, fileObj, selectedPath, showAllEdges)

    # set position and edge variables
    pos = nx.get_node_attributes(G, "pos")
    edges = G.edges()
    edge_color = [G[u][v]["color"] for u, v in edges]

    # show edge weights if variable true
    if showWeights:
        labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(
            G,
            pos,
            edge_labels=labels,
            font_size=6,
            alpha=0.4,
            font_weight=0.1,
            label_pos=0.5,
        )

    # draw the graph with desired attributes
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=140,
        font_size=7,
        node_color="#ccccff",
        linewidths=node_edge_width,
        edgecolors=node_edge_color,
        width=edge_width,
        edge_color=edge_color,
    )

    # display graph screen
    plt.show()


if __name__ == "__main__":
    main()
