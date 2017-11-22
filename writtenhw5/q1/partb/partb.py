import graph_for_plot as gplot
import matplotlib.pyplot as pyplot
import math


def likelihood(y, n, theta):
    return (
        math.factorial(n) / (math.factorial(n-y) * math.factorial(y))
        * math.pow(theta, y)
        * math.pow((1 - theta), n - y)
    )


x, y = gplot.graph_function(0, 4, 1, likelihood, 4, .75)

pyplot.xlabel("y")
pyplot.ylabel("p(y|θ,n)")
pyplot.bar(x, y)
pyplot.show()
