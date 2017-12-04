from collections import namedtuple
from matplotlib import pyplot
import random
import math
import scipy.misc

# constant declarations
BinomialHypothesis = namedtuple('BinomialHypothesis', 'name, theta, probability')
random.seed(2051)  # I again set the seed to a hardcoded value for consistent results


# for each hypothesis being true, generate the probability curve of each hypothesis
def generate_probability_graphs(hypotheses, averaging):
    assert isinstance(hypotheses, tuple)

    nrows, ncols = 2, 3
    fig, axes = pyplot.subplots(nrows=nrows, ncols=ncols)
    fig2, axes2 = pyplot.subplots(nrows=nrows, ncols=ncols)
    pyplot.tight_layout()
    h_plots = [axes[0, 0], axes[0, 1], axes[0, 2], axes[1, 0], axes[1, 1]]
    next_d_plots = [axes2[0, 0], axes2[0, 1], axes2[0, 2], axes2[1, 0], axes2[1, 1]]

    for i in range(len(hypotheses)):
        data_count = 100
        dataset = list(generate_dataset(hypotheses[i], data_count))
        posteriors = list(generate_posteriors(hypotheses, list(generate_favorable_outcomes(dataset))))
        if averaging:
            dataset2 = list(generate_dataset(hypotheses[i], data_count))
            posteriors2 = list(generate_posteriors(hypotheses, list(generate_favorable_outcomes(dataset2))))
            posteriors[i] = [(posteriors[i][n] + posteriors2[i][n]) / 2.0 for n in range(len(posteriors[i]))]
        probabilities_next_value_false = generate_probability_next_value_false(hypotheses, posteriors)
        for j in range(len(posteriors)):
            label = "h" + str(j+1)
            print(label)
            h_plots[i].plot(range(data_count), posteriors[j], label=label)
            h_plots[i].legend()
        next_d_plots[i].plot(range(data_count), probabilities_next_value_false)
    pyplot.show()


def generate_posteriors(h, y):

    # indexed by h, then n
    posteriors = []
    for hi in h:
        posteriors.append([])

    for n in range(len(y)):
        normalizing_constant = 0
        unnormalized_posteriors = []
        for i in range(len(h)):
            likelihood = scipy.misc.comb(n+1, y[n]) * math.pow(h[i].theta, y[n]) * math.pow(1-h[i].theta, n+1-y[n])
            normalizing_constant += likelihood * h[i].probability
            unnormalized_posteriors.append(likelihood * h[i].probability)
        for i in range(len(h)):
            posteriors[i].append(unnormalized_posteriors[i]/normalizing_constant)
    return posteriors


def generate_probability_next_value_false(h, posteriors):

    probabilities_next_value_false = []
    for n in range(len(posteriors[0])):
        sum_probabilities = 0
        for i in range(len(h)):
            sum_probabilities += posteriors[i][n] * (1-h[i].theta)
        probabilities_next_value_false.append(sum_probabilities)
    return probabilities_next_value_false


def generate_dataset(hypothesis, data_count):
    assert isinstance(hypothesis, BinomialHypothesis)
    assert isinstance(data_count, int)

    for i in range(data_count):
        yield (random.random() < hypothesis.theta)


def generate_favorable_outcomes(dataset):
    y = 0
    for n in range(len(dataset)):
        if dataset[n]:
            y += 1
        yield y


# probabilities for the bags o' surprise problem, by P(cherry)
h1 = BinomialHypothesis(name='h1', theta=1.0, probability=.1)
h2 = BinomialHypothesis(name='h2', theta=.75, probability=.2)
h3 = BinomialHypothesis(name='h3', theta=.5, probability=.4)
h4 = BinomialHypothesis(name='h4', theta=.25, probability=.2)
h5 = BinomialHypothesis(name='h5', theta=0.0, probability=.1)


generate_probability_graphs((h1, h2, h3, h4, h5), False)
generate_probability_graphs((h1, h2, h3, h4, h5), True)

