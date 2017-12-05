import matplotlib.pyplot as pyplot
import random
import IrisDataPlotter as iris
from scipy.spatial import distance


def initialize_means(k, data):
    random.seed(1025)
    means = []
    for i in range(k):
        means.append([random.uniform(min(data[0]), max(data[0])), random.uniform(min(data[1]), max(data[1]))])
    return means


def update_means(u, x):
    assert isinstance(u, list)

    new_u = [] # indexed by dimension
    for u_k in u:
        numerator = [0] * len(u_k) # indexed by dimension
        denominator = 0
        for n in range(len(x[0])):
            closest_u = closest_mean([x[dim][n] for dim in range(len(x))], u)
            if closest_u == u_k:
                denominator += 1
                for dim in range(len(x)):
                    numerator[dim] += x[dim][n]
        new_u.append([numerator[i]/denominator for i in range(len(numerator))])
    return new_u


def closest_mean(xn, u):
    assert isinstance(u, list)

    closest_u = u[0]
    closest_u_distance = distance.euclidean(u[0], xn)
    for u_k in u:
        u_distance = distance.euclidean(u_k, xn)
        if u_distance < closest_u_distance:
            closest_u_distance = u_distance
            closest_u = u_k
    return closest_u


def plot_means(subplot, means):
    for mean in means:
        subplot.scatter(mean[0], mean[1], marker='P', color='black')


def plot_versicolor_and_virginica(subplot, means):
    subplot.scatter(iris.versicolor_xs, iris.versicolor_ys, label='Versicolor')
    subplot.scatter(iris.virginica_xs, iris.virginica_ys, label='Virginica')
    plot_means(subplot, means)


def plot_all(subplot, means):
    subplot.scatter(iris.flower_xs, iris.flower_ys)
    plot_means(subplot, means)


def plot_convergence(k, data, subplots, plot):
    means = list(initialize_means(k, data))
    plot(subplots[0], means)
    for i in range(5):
        means = update_means(means, data)
        if i == 2:
            plot(subplots[1], means)
    plot(subplots[2], means)


def plot_for_2_and_3_k(data, plot):
    fig, axes = pyplot.subplots(2, 3)
    k_2_subplots = (axes[0][0], axes[0][1], axes[0][2])
    k_3_subplots = (axes[1][0], axes[1][1], axes[1][2])
    plot_convergence(2, data, k_2_subplots, plot)
    plot_convergence(3, data, k_3_subplots, plot)
    iris.show_plot()


iris.load_iris_data()
data = (iris.versicolor_xs + iris.virginica_xs, iris.versicolor_ys + iris.virginica_ys)
plot_for_2_and_3_k(data, plot_versicolor_and_virginica)
iris.load_iris_data_all_species()
data = (iris.flower_xs, iris.flower_ys)
plot_for_2_and_3_k(data, plot_all)
