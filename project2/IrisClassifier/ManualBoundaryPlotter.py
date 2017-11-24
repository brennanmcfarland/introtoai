import csv
import matplotlib.pyplot as pyplot
import enum


# ASSIGNMENT 1a.
Classification = enum.Enum('Classification', 'VERSICOLOR VIRGINICA')


# ASSIGNMENT 1b.
def linear_decision_boundary(x):
    # linear, y=mx+b
    return -1.4*x+8.44


def plot_linear_decision_boundary():
    x = (4.1, 5.4)
    y = (linear_decision_boundary(x[0]), linear_decision_boundary(x[1]))
    pyplot.plot(x, y)


# ASSIGNMENT 1c.
def classify(x, y):
    if y > linear_decision_boundary(x):
        return Classification.VIRGINICA
    else:
        return Classification.VERSICOLOR


def plot_classifier_examples():
    new_versicolor_xs = []
    new_versicolor_ys = []
    new_virginica_xs = []
    new_virginica_ys = []
    example_xs = [float(i) for i in versicolor_xs[:3]] + [float(i) for i in virginica_xs[:3]]
    print(example_xs)
    example_ys = [float(i) for i in versicolor_ys[:3]] + [float(i) for i in virginica_ys[:3]]
    for i in range(len(example_xs)):
        if classify(example_xs[i], example_ys[i]) == Classification.VERSICOLOR:
            new_versicolor_xs.append(example_xs[i])
            new_versicolor_ys.append(example_ys[i])
        else:
            new_virginica_xs.append(example_xs[i])
            new_virginica_ys.append(example_ys[i])
    pyplot.scatter(new_versicolor_xs, new_versicolor_ys, label='Versicolor')
    pyplot.scatter(new_virginica_xs, new_virginica_ys, label='Virginica')
    plot_linear_decision_boundary()


# ASSIGNMENT 1a.

def show_plot():
    pyplot.legend()
    pyplot.tight_layout()
    pyplot.xlabel('petal length (cm)')
    pyplot.ylabel('petal width (cm)')
    pyplot.show()

versicolor_xs = []
versicolor_ys = []
virginica_xs = []
virginica_ys = []
with open('irisdata.csv', newline='') as csvfile:
    csvreader = csv.DictReader(csvfile)
    # line should be an ordered dict of col values indexed by the header row
    for line in csvreader:
        if line['species'] == "versicolor":
            versicolor_xs.append(line['petal_length'])
            versicolor_ys.append(line['petal_width'])
        elif line['species'] == "virginica":
            virginica_xs.append(line['petal_length'])
            virginica_ys.append(line['petal_width'])

pyplot.scatter(versicolor_xs, versicolor_ys, label='Versicolor')
pyplot.scatter(virginica_xs, virginica_ys, label='Virginica')
plot_linear_decision_boundary()  # ASSIGNMENT 1b.
show_plot()

# ASSIGNMENT 1c.
plot_classifier_examples()
show_plot()