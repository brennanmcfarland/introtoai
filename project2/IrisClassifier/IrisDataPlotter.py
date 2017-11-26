import csv
import matplotlib.pyplot as pyplot


versicolor_xs = []
versicolor_ys = []
virginica_xs = []
virginica_ys = []


def load_iris_data():
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


def show_plot():
    for subplot in pyplot.gcf().get_axes():
        subplot.legend()
        pyplot.tight_layout()
        subplot.set_xlabel('petal length (cm)')
        subplot.set_ylabel('petal width (cm)')
    pyplot.show()