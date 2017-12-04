import matplotlib.pyplot as pyplot
import random
import IrisDataPlotter as iris
from scipy.spatial import distance


NUM_CLUSTERS = 2


def initialize_means(data):
    random.seed(1025)
    means = []
    for i in range(NUM_CLUSTERS):
        means.append([random.uniform(min(data[0]), max(data[0])), random.uniform(min(data[1]), max(data[1]))])
    return means


# TODO: fix and finish implementing for an arbitrary number of dimensions (use helper functions)
def update_means(u, x):
    assert isinstance(u, list)

    new_u = [] # indexed by dimension
    for u_k in u:
        numerator = [] # indexed by dimension
        denominator = []
        for dim in range(len(u_k)):
            numerator.append(0.0)
            denominator.append(0.0)
        for n in range(len(x[0])):
            closest_u = closest_mean([x[dim][n] for dim in range(len(x))], u)
            r_nk = 1.0 if closest_u == u_k else 0
            if r_nk == 1.0:
                for dim in range(len(x)):
                    numerator[dim] += x[dim][n]
                    denominator[dim] += 1.0
        new_u.append([numerator[i]/denominator[i] for i in range(len(numerator))])
    return new_u

        # for i in range(len(uk)):
        #     update_means_dimension(means, i)


# def update_means_dimension(i):
#     numerator = 0.0
#     denominator = 0.0
#     for n in range(len(data[i])):
#         numerator += data[i][n] * 2  # TODO: what is the correct value for r_n,k? (instead of 2)
#         denominator += 2  # TODO: same as above
#     return numerator / denominator


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


def is_closest_to(k):

    pass  # TODO: implement, may want to talk to others to make sure this is the right equation
    # TODO: before proceeding


# TODO: get it to plot for arbitrary # dimensions?
def plot_means():
    for mean in means:
        pyplot.scatter(mean[0], mean[1], marker='P')


def plot_and_show():
    pyplot.scatter(iris.versicolor_xs, iris.versicolor_ys, label='Versicolor')
    pyplot.scatter(iris.virginica_xs, iris.virginica_ys, label='Virginica')
    plot_means()
    iris.show_plot()


iris.load_iris_data()

data = (iris.versicolor_xs + iris.virginica_xs, iris.versicolor_ys + iris.virginica_ys)
means = list(initialize_means(data))
for i in range(12):
    means = update_means(means, data)
        plot_and_show()
