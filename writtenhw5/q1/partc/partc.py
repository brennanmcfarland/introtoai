import graph_for_plot as gplot
import matplotlib.pyplot as pyplot
import math

PLOT_RESOLUTION = .01


def posterior(theta, y, n):
    return (
        (1 + n)
        * math.factorial(n) / (math.factorial(n - y) * math.factorial(y))
        * math.pow(theta, y)
        * math.pow((1 - theta), n - y)
    )


def plot_subplot(subplot, x, y, title):
    subplot.plot(x, y)
    subplot.set_xlabel("θ")
    subplot.set_title(title)


f, axes = pyplot.subplots(nrows=2, ncols=2)
pyplot.tight_layout()

x, y = gplot.graph_function(0, 1, PLOT_RESOLUTION, posterior, 1, 1)
plot_subplot(axes[0, 0], x, y, "head")

x, y = gplot.graph_function(0, 1, PLOT_RESOLUTION, posterior, 2, 2)
plot_subplot(axes[0, 1], x, y, "head, head")

x, y = gplot.graph_function(0, 1, PLOT_RESOLUTION, posterior, 2, 3)
plot_subplot(axes[1, 0], x, y, "head, head, tail")

x, y = gplot.graph_function(0, 1, PLOT_RESOLUTION, posterior, 3, 4)
plot_subplot(axes[1, 1], x, y, "head, head, tail, head")

pyplot.show()
