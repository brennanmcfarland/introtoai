import IrisDataPlotter as iris
import matplotlib.pyplot as pyplot


RADIUS = 1.0
w = [-2, 8]
weights = [8.5, -1.5]


# ASSIGNMENT 2e.
def learned_decision_boundary(x):
    return weights[1]*x+weights[0]


# ASSIGNMENT 1b.
def linear_decision_boundary(x):
    # linear, y=mx+b
    return -1.4*x+8.44


# ASSIGNMENT 2b.
def bad_linear_decision_boundary(x):
    return -.6*x+6


# ASSIGNMENT 1b.
def plot_linear_decision_boundary(boundary_function, subplot):
    x = (4.1, 5.4)
    y = (boundary_function(x[0]), boundary_function(x[1]))
    subplot.plot(x, y)


# ASSIGNMENT 1c.
def plot_circle_boundary(centerx, centery, subplot):
    circle = pyplot.Circle((centerx, centery), RADIUS, facecolor='none', edgecolor='blue')
    subplot.add_patch(circle)


# ASSIGNMENT 1c.
def classify(x, y, decision_boundary):
    if y > decision_boundary(x):
        return iris.Classification.VIRGINICA
    else:
        return iris.Classification.VERSICOLOR


# ASSIGNMENT 2e.
def general_decision_threshold(data):
    sum = 0
    for i in range(len(weights)):
        sum += data[i] * weights[i]
    return sum


def classify_generally(data):
    if general_decision_threshold(data) < data[-1]:
        return 1
    else:
        return 0


# ASSIGNMENT 1d.
def radially_classify(x, y, centerx, centery):
    if (x-centerx)*(x-centerx) + (y-centery)*(y-centery) < RADIUS:
        return iris.Classification.VIRGINICA
    else:
        return iris.Classification.VERSICOLOR

# ASSIGNMENT 2a.
# x: data vectors
# decision_boundary_function: a lambda for getting the y of the decision boundary given an x
# pattern_classes: the classes/pattern classes
def mean_squared_error(x, decision_boundary_function, correct_pattern_classes):
    # get the summation
    num_erroneous = 0
    for n in range(len(x)):
        if classify(x[n][0], x[n][1], decision_boundary_function) != correct_pattern_classes[n]:
            num_erroneous += 1
    return num_erroneous/len(x)


# ASSIGNMENT 2e.
def gradient(x, correct_pattern_classes):
    gradient_vector = []
    for i in range(len(weights)):
        gradient_dimension = 0
        for n in range(len(x)):
            sign = 0
            predicted_class = classify_generally(x[n])
            correct_class = correct_pattern_classes[n]
            if predicted_class != correct_class:
                if correct_pattern_classes[n] == 1:
                    sign = 1
                else:
                    sign = -1
            gradient_dimension += x[n][i] * sign
        gradient_dimension *= 2.0 / len(x) * .025 # step size
        gradient_vector.append(gradient_dimension)
    print(gradient_vector)
    return gradient_vector
