import matplotlib.pyplot as pyplot
import random
import IrisDataPlotter as iris


NUM_CLUSTERS = 2


# TODO: we could possibly use a lambda and pass it a parameter to reduce these 4 functions to one
def max_x():
    return max(max(iris.versicolor_xs), max(iris.virginica_xs))


def min_x():
    return min(min(iris.versicolor_xs), min(iris.virginica_xs))


def max_y():
    return max(max(iris.versicolor_ys), max(iris.virginica_ys))


def min_y():
    return min(min(iris.versicolor_ys), min(iris.virginica_ys))


def initialize_means():
    random.seed(1024)
    xs, ys = [], []
    for i in range(NUM_CLUSTERS):
        xs.append(random.uniform(min_x(), max_x()))
        ys.append(random.uniform(min_y(), max_y()))
    return xs, ys


def plot_means():
    for i in range(NUM_CLUSTERS):
        pyplot.scatter(mean_xs[i], mean_ys[i], marker='P')


iris.load_iris_data()
pyplot.scatter(iris.versicolor_xs, iris.versicolor_ys, label='Versicolor')
pyplot.scatter(iris.virginica_xs, iris.virginica_ys, label='Virginica')

mean_xs, mean_ys = initialize_means()
plot_means()


iris.show_plot()
