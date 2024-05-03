import tkinter as tk

# import os


class Gui:
    guiArray = []

    def guiCreate(self):

        window = tk.Tk()

        label = tk.Label(window, text="File Name")
        label.place(x=65, y=50)

        entry = tk.Entry(window)
        entry.insert(-1, "input10.txt")
        entry.grid(row=0, column=1)
        entry.place(x=140, y=50)

        label = tk.Label(window, text="Algorithm")
        label.place(x=65, y=85)

        opt = [
            "MST (Prims)",
            "MST (Kruskal)",
            "SPT (Dijkstra)",
            "SPT (Bellman Ford)",
            "SPT (Floyd)",
        ]
        varDrop = tk.StringVar(window)
        varDrop.set(opt[0])
        drop = tk.OptionMenu(window, varDrop, *opt)
        drop.place(x=140, y=80)

        varEdge = tk.IntVar()
        varWeight = tk.IntVar()
        edge = tk.Checkbutton(window, text="Show All Edges", variable=varEdge)
        weight = tk.Checkbutton(window, text="Show Edge Weights", variable=varWeight)
        edge.place(x=100, y=140)
        weight.place(x=100, y=160)

        def getGuiInput():
            temp = varDrop.get()
            for i in range(len(opt)):
                if opt[i] == temp:
                    self.guiArray = [entry.get(), i, varEdge.get(), varWeight.get()]
                    window.destroy()

        button = tk.Button(window, text="Generate Graph", width=25, command=getGuiInput)
        button.place(x=80, y=200)

        window.title("Graph")
        window.geometry("400x300+10+10")
        window.mainloop()
