import sys
import time
import os
import pandas as pd
import csv
from random import randint
import pyqtgraph as pg
from PyQt5 import QtWidgets, QtCore

class Graph(QtWidgets.QWidget):
    def __init__(self, widget, live_plot):
        super(Graph, self).__init__()

        self.live_plot = live_plot
        self.line = None

        self.resize(580, 458)
        self.setObjectName("Graph")
        self.gridLayout = QtWidgets.QGridLayout(widget)
        self.gridLayout.setObjectName("gridLayout")

        # Temperature vs time dynamic plot
        self.plot_graph = pg.PlotWidget()
        #self.setCentralWidget(self.plot_graph)
        self.gridLayout.addWidget(self.plot_graph, 0, 0, 1, 1)
        self.plot_graph.setBackground("w")
        self.plot_graph.setTitle("Temperature vs Time", color="b", size="20pt")
        styles = {"color": "blue", "font-size": "18px"}
        self.plot_graph.setLabel("left", "Temperature (°C)", **styles)
        self.plot_graph.setLabel("bottom", "Time (min)", **styles)
        self.plot_graph.addLegend()
        self.plot_graph.showGrid(x=True, y=True)
        self.plot_graph.setYRange(10, 20)

    def delete_data(self):
        if(True == self.live_plot):
            self.timer.stop()
        
        self.line.clear()
        print("I'm being automatically destroyed. Goodbye!")

    def start(self, file_path):
        self.file_path = file_path

        self.update_data()

        if(True == self.live_plot):
            # Add a timer to simulate new temperature measurements
            self.timer = QtCore.QTimer()
            self.timer.setInterval(50)
            self.timer.timeout.connect(self.update_plot)
            self.timer.start()

    def update_plot(self):
        #self.time = self.time[1:]
        #self.time.append(self.time[-1] + 1)
        #self.temperature = self.temperature[1:]
        #self.temperature.append(randint(20, 40))
        self.update_data()
        #self.line.setData(self.time, self.temperature)
        if(None != self.line):
            self.line.setData(self.df[:,0], self.df[:,1])

    def update_data(self):
        file_size = os.path.getsize(self.file_path)
        if(0 != file_size):
            self.df = pd.read_csv(self.file_path, sep=',', header=None)
            self.df = self.df.values
            pen = pg.mkPen(color=(255, 0, 0))
            if(None == self.line):
                self.line = self.plot_graph.plot(
                    self.df[:,0],
                    self.df[:,1],
                    name="Temperature Sensor",
                    pen=pen,
                    #symbol="+",
                    #symbolSize=15,
                    #symbolBrush="b",
                )
            else:
                self.line = self.plot_graph.plot(
                    self.df[:,0],
                    self.df[:,1],
                    pen=pen,
                )
