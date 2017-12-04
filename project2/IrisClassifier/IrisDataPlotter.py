import csv
import enum
import matplotlib.pyplot as pyplot


# ASSIGNMENT 1a.
Classification = enum.Enum('Classification', 'VERSICOLOR VIRGINICA')

flower_xs = []
flower_ys = []
versicolor_xs = []
versicolor_ys = []
virginica_xs = []
virginica_ys = []


# ASSIGNMENT 1a.
def load_iris_data():
    with open('irisdata.csv', newline='') as csvfile:
        csvreader = csv.DictReader(csvfile)
        # line should be an ordered dict of col values indexed by the header row
        for line in csvreader:
            if line['species'] == "versicolor":
                versicolor_xs.append(float(line['petal_length']))
                versicolor_ys.append(float(line['petal_width']))
            elif line['species'] == "virginica":
                virginica_xs.append(float(line['petal_length']))
                virginica_ys.append(float(line['petal_width']))


#ASSIGNMENT Written 4b
def load_iris_data_all_species():
    with open('irisdata.csv', newline='') as csvfile:
        csvreader = csv.DictReader(csvfile)
        # line should be an ordered dict of col values indexed by the header row
        for line in csvreader:
            flower_xs.append(float(line['petal_length']))
            flower_ys.append(float(line['petal_width']))


# ASSIGNMENT 1a.
def show_plot():
    for subplot in pyplot.gcf().get_axes():
        subplot.legend()
        pyplot.tight_layout()
        subplot.set_xlabel('petal length (cm)')
        subplot.set_ylabel('petal width (cm)')
    pyplot.show()