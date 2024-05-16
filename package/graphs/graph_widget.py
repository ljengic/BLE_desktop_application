import sys
import time
from PyQt5 import QtWidgets, QtCore
from package.graphs.gui_graph_widget import Ui_Graph_widget
from package.graphs.graph import Graph
from package.graphs.check_box_widget import Check_Box_Widget

def column(matrix, i):
    return [row[i] for row in matrix]

class Graph_Widget(QtWidgets.QWidget, Ui_Graph_widget):
    def __init__(self, parent, live_plot):
        super(Graph_Widget, self).__init__(parent)
        self.setupUi(self)

        self.live_plot = live_plot

        self.graph = Graph(self.widget, self.live_plot)

    # elementi liste su [ime, putanja]
    def set_lines(self,list_of_lines):
        self.lines = list_of_lines
        self.check_box_list = []
        self.check_box_widget_list = []
        self.graph.set_plot_data(self.lines)
        print("tu cemo napravit desno izbornik i podesit putanje")
        for line in self.lines:
            print(line)
            newCheck = Check_Box_Widget(self.frame, line[0], line[2])
            self.verticalLayout.addWidget(newCheck)
            self.check_box_widget_list.append(newCheck)
            self.check_box_list.append(newCheck.checkBox)
            self.check_box_list[-1].stateChanged.connect(self.checkBox_state_change_handle)

        self.checkBox_state_change_handle()

    #b is checkBox which state changed
    def checkBox_state_change_handle(self):
        self.show_list = []
        for check_box in self.check_box_list:
            if (True == check_box.isChecked()):
                self.show_list.append(True)
                
            else:
                self.show_list.append(False)
        self.graph.update_enabled(self.show_list)

        self.check_box_widget_set_background(self.show_list)

    #change background colors
    def check_box_widget_set_background(self, enabled_list):
        i=0
        for check_box_widget in self.check_box_widget_list:
            check_box_widget.change_bakground_color(enabled_list[i])
            i=i+1

    def start(self):
        self.graph.start()

    def stop(self):
        self.graph.delete_data()

        for w in self.check_box_widget_list:
            #self.verticalLayout.removeItem(w)
            w.hide()
            del w

    def get_max_time(self):
        return self.graph.get_max_time()

    def move_to_next_window(self):
        self.graph.move_to_next_window()

