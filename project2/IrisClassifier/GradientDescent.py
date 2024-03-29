import IrisDataPlotter as iris
import Boundary as boundary
import matplotlib.pyplot as pyplot
import random

# ASSIGNMENT 3.
iris.load_iris_data()
data_vectors = [[iris.versicolor_xs[d], iris.versicolor_ys[d]] for d in range(len(iris.versicolor_xs))]\
               + [[iris.virginica_xs[d], iris.virginica_ys[d]] for d in range(len(iris.virginica_xs))]
correct_classification = [iris.Classification.VERSICOLOR for c in range(len(iris.versicolor_xs))]\
                         + [iris.Classification.VIRGINICA for c in range(len(iris.virginica_xs))]

random.seed = 2083
boundary.weights = [random.uniform(0, 10), random.uniform(-10, 0)]
error_plot_values = []
iteration = 0
while iteration < 10000:
    error_plot_values.append(boundary.mean_squared_error(data_vectors, boundary.learned_decision_boundary, correct_classification))

    if iteration % 20 == 0 or error_plot_values[-1] < .15:
        boundary.plot_linear_decision_boundary(boundary.learned_decision_boundary, pyplot)
        pyplot.scatter(iris.versicolor_xs, iris.versicolor_ys, label='Versicolor')
        pyplot.scatter(iris.virginica_xs, iris.virginica_ys, label='Virginica')
        iris.show_plot()

        pyplot.plot(range(len(error_plot_values)), error_plot_values)
        pyplot.show()

    gradient = boundary.gradient([[1] + d for d in data_vectors], [1 if i == iris.Classification.VERSICOLOR else 0
                                                                for i in correct_classification])
    print(gradient)
    boundary.weights = [boundary.weights[i] - gradient[i] for i in range(len(gradient))]

    if error_plot_values[-1] < .15:
        break
    iteration += 1
    print(iteration)
