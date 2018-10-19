import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class PlotWidget(FigureCanvas):

    def __init__(self, parent):
        figure = Figure(dpi=100)
        super().__init__(figure)
        self.ax = self.figure.add_subplot(111)
        self.setParent(parent)

    def setLegend(self, title, x_label, y_label):
        self.ax.set_title(title)
        self.ax.set_xlabel(x_label)
        self.ax.set_ylabel(y_label)

    def plotData(self, data, label=None, color='red'):
        data = np.array(data)
        x = data[:, 0].flatten()
        y = data[:, 1].flatten()
        self.ax.plot(x, y, label=label, color=color)
        self.ax.grid(True)
        self.ax.legend()