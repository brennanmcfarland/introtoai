from collections import namedtuple
from matplotlib import pyplot
import random
import math

# constant declarations
BinomialHypothesis = namedtuple('BinomialHypothesis', 'name, theta')


# TODO: it's supposed to make 4 graphs, 1 for each hypothesis being correct, and EACH GRAPH SHOULD
# TODO: HAVE 5 LINES FOR THE PROBABILITY OF EACH HYPOTHESIS, fix that

# for each hypothesis, generate its curve
def generate_probability_graphs(hypotheses):
    assert isinstance(hypotheses, tuple)

    for hypothesis in hypotheses:
        data_count = 100
        dataset = list(generate_dataset(hypothesis, data_count))
        log_alpha = generate_log_alpha(dataset, hypotheses)
        #print(dataset)
        yield generate_probability_graph(hypotheses, hypothesis, dataset, log_alpha)


def generate_probability_graph(hypotheses, correct_hypothesis, dataset, log_alpha):
    assert isinstance(hypotheses, tuple)
    assert isinstance(correct_hypothesis, BinomialHypothesis)

    for hypothesis in hypotheses:
        yield generate_probability_curve(hypotheses, correct_hypothesis, hypothesis, dataset, log_alpha)


def generate_probability_curve(hypotheses, correct_hypothesis, this_hypothesis, dataset, log_alpha):
    assert isinstance(hypotheses, tuple)
    assert isinstance(correct_hypothesis, BinomialHypothesis)
    assert isinstance(this_hypothesis, BinomialHypothesis)

    # iteratively do this on increasing portions of the list
    posteriors = list(generate_posteriors(this_hypothesis, len(hypotheses), dataset, log_alpha))
    #print(posteriors)
    return range(len(dataset)), posteriors


def generate_dataset(hypothesis, data_count):
    assert isinstance(hypothesis, BinomialHypothesis)
    assert isinstance(data_count, int)

    random.seed(2049)  # I again set the seed to a hardcoded value for consistent results
    for i in range(data_count):
        yield (random.random() < hypothesis.theta)


def generate_alpha(dataset, hypotheses):
    assert isinstance(hypotheses, tuple)

    return math.pow(math.e, generate_log_alpha(dataset, hypotheses))


def generate_log_alpha(dataset, hypotheses):
    assert isinstance(hypotheses, tuple)

    outer_sum = 0.0
    for i in range(len(dataset)):
        inner_sum = 0.0
        for j in range(len(hypotheses)):
            inner_sum += p_d_given_h(dataset[i], hypotheses[j])
        outer_sum += math.log(inner_sum)

    return math.log(len(hypotheses)) - outer_sum


def generate_posteriors(hypothesis, num_hypotheses, dataset, alpha):
    for i in range(len(dataset)):
        yield generate_posterior(hypothesis, num_hypotheses, dataset[:i + 1], alpha)


def generate_posterior(hypothesis, num_hypotheses, dataset, log_alpha):
    sum = 0.0
    for i in range(len(dataset)):
        # TODO: is the sum overflowing?
        print(sum)
        sum += math.log(p_d_given_h(dataset[i], hypothesis))
    log_posterior = -math.log(num_hypotheses) + log_alpha + sum
    return math.pow(math.e, log_posterior)


def generate_prob_next_datapoint():
    # TODO: implement
    pass


def p_d_given_h(d, h):
    assert isinstance(d, bool)
    assert isinstance(h, BinomialHypothesis)

    if d:
        return h.theta
    else:
        return 1.0 - h.theta


def plot_row(row, num_cols, x, y):
    for i in range(num_cols):
        row[i].plot(x, y)


# probabilities for the bags o' surprise problem, by P(cherry)
h1 = BinomialHypothesis(name='h1', theta=1.0)
h2 = BinomialHypothesis(name='h2', theta=.75)
h3 = BinomialHypothesis(name='h3', theta=.25)
h4 = BinomialHypothesis(name='h4', theta=0.0)


nrows, ncols = 2, 2
fig, axes = pyplot.subplots(nrows=nrows, ncols=nrows)
pyplot.tight_layout()

h_plots = [axes[0, 0], axes[0, 1], axes[1, 0], axes[1, 1]]

probability_graphs = list(generate_probability_graphs((h1, h2, h3, h4)))
print(probability_graphs)
# TODO: now we just have to unpack the data from the generator functions and plot it
for h_graph in range(len(h_plots)):
    h_graph_plot = list(probability_graphs[h_graph])
    print(h_graph_plot)
    for h_curve in range(len(h_plots)):
        h_curve_plot = list(h_graph_plot[h_curve])
        h_plots[h_graph].plot(h_curve_plot[0], h_curve_plot[1])

pyplot.show()
