import matplotlib.pyplot as pyplot
import IrisDataPlotter as iris


RADIUS = 1.0


# ASSIGNMENT 1b.
def linear_decision_boundary(x):
    # linear, y=mx+b
    return -1.4*x+8.44


def plot_linear_decision_boundary():
    x = (4.1, 5.4)
    y = (linear_decision_boundary(x[0]), linear_decision_boundary(x[1]))
    pyplot.plot(x, y)


# ASSIGNMENT 1c.
def plot_circle_boundary(centerx, centery, subplot):
    circle = pyplot.Circle((centerx, centery), RADIUS, facecolor='none', edgecolor='blue')
    subplot.add_patch(circle)


def classify(x, y):
    if y > linear_decision_boundary(x):
        return iris.Classification.VIRGINICA
    else:
        return iris.Classification.VERSICOLOR


# ASSIGNMENT 1d.
def radially_classify(x, y, centerx, centery):
    if (x-centerx)*(x-centerx) + (y-centery)*(y-centery) < RADIUS:
        return iris.Classification.VIRGINICA
    else:
        return iris.Classification.VERSICOLOR


def graph_radial_classification_class_at_center(centerx, centery, input_xs, input_ys, correct_class):
    correct_xs = []
    correct_ys = []
    incorrect_xs = []
    incorrect_ys = []
    for i in range(len(input_xs)):
        if radially_classify(input_xs[i], input_ys[i], centerx, centery) == correct_class:
            correct_xs.append(input_xs[i])
            correct_ys.append(input_ys[i])
        else:
            incorrect_xs.append(input_xs[i])
            incorrect_ys.append(input_ys[i])

    print(len(incorrect_xs))
    return correct_xs, correct_ys, incorrect_xs, incorrect_ys


def plot_radial_classification_at_center(centerx, centery, subplot):
    input_xs = iris.versicolor_xs
    input_ys = iris.versicolor_ys
    correct_xs, correct_ys, incorrect_xs, incorrect_ys = graph_radial_classification_class_at_center(
        centerx, centery, input_xs, input_ys, iris.Classification.VERSICOLOR)
    print(len(incorrect_ys))
    subplot.scatter(correct_xs, correct_ys, label='Versicolor', color='blue')
    subplot.scatter(incorrect_xs, incorrect_ys, label='Versicolor (erroneous)', color='green')
    input_xs = iris.virginica_xs
    input_ys = iris.virginica_ys
    correct_xs, correct_ys, incorrect_xs, incorrect_ys = graph_radial_classification_class_at_center(
        centerx, centery, input_xs, input_ys, iris.Classification.VIRGINICA)
    subplot.scatter(correct_xs, correct_ys, label='Virginica', color='orange')
    subplot.scatter(incorrect_xs, incorrect_ys, label='Virginica (erroneous)', color='red')
    plot_circle_boundary(centerx, centery, subplot)


def plot_radial_classification():
    fig, axes = pyplot.subplots(2, 2)
    plot_radial_classification_at_center(5.7, 2.0, axes[0, 0])
    plot_radial_classification_at_center(6.0, 2.2, axes[0, 1])
    plot_radial_classification_at_center(5.2, 1.7, axes[1, 0])


# ASSIGNMENT 1c.
def plot_classifier_examples():
    new_versicolor_xs = []
    new_versicolor_ys = []
    new_virginica_xs = []
    new_virginica_ys = []
    example_xs = iris.versicolor_xs[:3] + iris.virginica_xs[:3]
    print(example_xs)
    example_ys = iris.versicolor_ys[:3] + iris.virginica_ys[:3]
    for i in range(len(example_xs)):
        if classify(example_xs[i], example_ys[i]) == iris.Classification.VERSICOLOR:
            new_versicolor_xs.append(example_xs[i])
            new_versicolor_ys.append(example_ys[i])
        else:
            new_virginica_xs.append(example_xs[i])
            new_virginica_ys.append(example_ys[i])
    pyplot.scatter(new_versicolor_xs, new_versicolor_ys, label='Versicolor')
    pyplot.scatter(new_virginica_xs, new_virginica_ys, label='Virginica')
    plot_linear_decision_boundary()


# ASSIGNMENT 1a.
iris.load_iris_data()

pyplot.scatter(iris.versicolor_xs, iris.versicolor_ys, label='Versicolor')
pyplot.scatter(iris.virginica_xs, iris.virginica_ys, label='Virginica')
plot_linear_decision_boundary()  # ASSIGNMENT 1b.
iris.show_plot()

# ASSIGNMENT 1c.
plot_classifier_examples()
iris.show_plot()

# ASSIGNMENT 1d.
plot_radial_classification()
iris.show_plot()
