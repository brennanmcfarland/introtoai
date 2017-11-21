from collections import namedtuple
import random

# constant declarations
BinomialHypothesis = namedtuple('BinomialHypothesis', 'name, theta')
alpha = 1.0  # TODO: what is alpha's real value?


def generate_probability_graphs(hypothesis):
    assert isinstance(hypothesis, BinomialHypothesis)

    data_count = 100
    dataset = list(generate_dataset(hypothesis, data_count))
    print(dataset)

    posteriors = list(generate_posteriors(hypothesis, data_count))
    print(posteriors)


def generate_dataset(hypothesis, data_count):
    assert isinstance(hypothesis, BinomialHypothesis)
    assert isinstance(data_count, int)

    random.seed(2049)  # I again set the seed to a hardcoded value for consistent results
    for i in range(data_count):
        yield (random.random() < hypothesis.theta)


def generate_posteriors(hypothesis, data_count):
    for i in range(data_count):
        yield alpha  # what is the rest of this expression supposed to be? * 2 * hypothesis.theta


# probabilities for the bags o' surprise problem, by P(cherry)
h1 = BinomialHypothesis(name='h1', theta=1.0)
generate_probability_graphs(h1)
h2 = BinomialHypothesis(name='h2', theta=.75)
generate_probability_graphs(h2)
h3 = BinomialHypothesis(name='h3', theta=.25)
generate_probability_graphs(h3)
h4 = BinomialHypothesis(name='h4', theta=0.0)
generate_probability_graphs(h4)
