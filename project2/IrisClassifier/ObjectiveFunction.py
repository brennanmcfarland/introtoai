import IrisDataPlotter as iris
import Boundary as boundary
import matplotlib.pyplot as pyplot


# ASSIGNMENT 2a.
iris.load_iris_data()
data_vectors = [[iris.versicolor_xs[d], iris.versicolor_ys[d]] for d in range(len(iris.versicolor_xs))]\
               + [[iris.virginica_xs[d], iris.virginica_ys[d]] for d in range(len(iris.virginica_xs))]
correct_classification = [iris.Classification.VERSICOLOR for c in range(len(iris.versicolor_xs))]\
                         + [iris.Classification.VIRGINICA for c in range(len(iris.virginica_xs))]
print(boundary.mean_squared_error(data_vectors, boundary.linear_decision_boundary, correct_classification))
print(boundary.mean_squared_error(data_vectors, boundary.bad_linear_decision_boundary, correct_classification))

# ASSIGNMENT 2b.
boundary.plot_linear_decision_boundary(boundary.linear_decision_boundary, pyplot)
pyplot.plot((5, 7), (boundary.bad_linear_decision_boundary(5), boundary.bad_linear_decision_boundary(7)))

iris.plot_iris_data()
iris.show_plot()

# ASSIGNMENT 2e.
boundary.plot_linear_decision_boundary(boundary.learned_decision_boundary, pyplot)
iris.plot_iris_data()
iris.show_plot()

gradient = boundary.gradient([[1] + d for d in data_vectors], [1 if i == iris.Classification.VERSICOLOR else 0
                                                               for i in correct_classification])
boundary.weights = [boundary.weights[i] + gradient[i] for i in range(len(gradient))]
for i in boundary.weights:
    print(i)
boundary.plot_linear_decision_boundary(boundary.learned_decision_boundary, pyplot)
iris.plot_iris_data()
iris.show_plot()