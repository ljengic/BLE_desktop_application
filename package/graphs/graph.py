import sys
import time
import os
import pandas as pd
import csv
from random import randint
import pyqtgraph as pg
from PyQt5 import QtWidgets, QtCore

def column(matrix, i):
    return [row[i] for row in matrix]

class Graph(QtWidgets.QWidget):
    def __init__(self, widget, live_plot):
        super(Graph, self).__init__()

        self.time_min = 0
        self.time_max = 30

        self.live_plot = live_plot
        self.line = None
        self.lines = []

        self.resize(580, 458)
        self.setObjectName("Graph")
        self.gridLayout = QtWidgets.QGridLayout(widget)
        self.gridLayout.setObjectName("gridLayout")

        # Temperature vs time dynamic plot
        self.plot_graph = pg.PlotWidget()
        #self.setCentralWidget(self.plot_graph)
        self.gridLayout.addWidget(self.plot_graph, 0, 0, 1, 1)
        self.plot_graph.setBackground("w")
        self.plot_graph.setTitle("Impedance vs Time", color="black", size="16pt")
        styles = {"color": "black", "font-size": "18px"}
        self.plot_graph.setLabel("left", "Impedance (Ω)", **styles)
        self.plot_graph.setLabel("bottom", "Time (s)", **styles)
        self.plot_graph.addLegend()
        self.plot_graph.showGrid(x=True, y=True)

        #disable zoom in y axis
        self.plot_graph.plotItem.setMouseEnabled(x=True,y=False) # Only allow zoom in X-axis

        #hide legend
        self.legend = self.plot_graph.addLegend()
        self.plot_graph.scene().removeItem(self.legend)

    def delete_data(self):
        if(True == self.live_plot):
            self.timer.stop()

        for line in self.lines:
            line[2].clear()
            self.plot_graph.removeItem(line[2])

        self.time_min = 0
        self.time_max = 30 

        self.lines = []
        print("I'm being automatically destroyed. Goodbye!")

    def set_plot_data(self, lines):
        self.lines_to_plot = lines
        self.set_paths(column(self.lines_to_plot,1))
        for line in self.lines_to_plot:
            self.create_line(line)
        print("lines made")
        print(self.lines)

    def set_paths(self, paths):
        self.paths = paths
        print(self.paths)

    def start(self):

        print("starting pplot")

        self.plot_graph.setYRange(0, 2000)
        self.update_plot()

        if(True == self.live_plot):
            self.time_min = 0
            self.time_max = 30 
            self.plot_graph.setXRange(self.time_min, self.time_max)
            # Add a timer to simulate new temperature measurements
            self.timer = QtCore.QTimer()
            self.timer.setInterval(500)
            self.timer.timeout.connect(self.update_plot)
            self.timer.start()

    def update_plot(self):
        #self.time = self.time[1:]
        #self.time.append(self.time[-1] + 1)
        #self.temperature = self.temperature[1:]
        #self.temperature.append(randint(20, 40))
        for line in self.lines:
            self.update_data(line)
            #print(line)
        #self.line.setData(self.time, self.temperature)
        #if(None != self.line):
        #   self.line.setData(self.df[:,0], self.df[:,1])

    def update_data(self, line):
        #print(line)
        file_size = os.path.getsize(line[1])
        if(0 != file_size):
            self.df = pd.read_csv(line[1], sep=',', header=None)
            self.df = self.df.values
            if(None != line[2]):
                #print("updating data")
                line[2].setData(self.df[:,0], self.df[:,1])

    def create_line(self, line):
        print("pravim liniju")
        print(line)
        file_size = os.path.getsize(line[1])
        #if(0 != file_size):
        #self.df = pd.read_csv(line[1], sep=',', header=None)
        #self.df = self.df.values
        #pen = pg.mkPen(color=(255, 0, 0))
        pen = line[2]
        self.curve = self.plot_graph.plot(
            [],[],
            #self.df[:,0],
            #self.df[:,1],
            name=line[0],
            pen=pen,
            #symbol="+",
            #symbolSize=15,
            #symbolBrush="b",
        )
        line_tmp = []
        line_tmp.append(line[0])
        line_tmp.append(line[1])
        line_tmp.append(self.curve)
        print(line_tmp)
        self.lines.append(line_tmp)

    def update_enabled(self,show_list):
        self.cnt = 0
        for line in self.lines:
            if(True == show_list[self.cnt]):
                line[2].show()
            else:
                line[2].hide()
            self.cnt = self.cnt + 1
    
    def move_to_next_window(self):
        if(True == self.live_plot):
            self.time_min = self.time_min + 30
            self.time_max = self.time_max + 30
            self.plot_graph.setXRange(self.time_min, self.time_max)


    def get_max_time(self):
        return self.time_max
 
