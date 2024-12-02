import csv
import numpy as np
import matplotlib.pyplot as plt

def plot_data(csv_file_path: str):
    """
    Plots the precision-recall curve from a .csv file.
    """
    results = []
    with open(csv_file_path, "r") as result_csv:
        csv_reader = csv.reader(result_csv, delimiter=',')
        next(csv_reader) 
        for row in csv_reader:
            results.append([float(row[0]), float(row[1])]) 
    
    results = np.array(results) 

    plt.plot(results[:, 1], results[:, 0])
    plt.ylim([-0.05, 1.05])
    plt.xlim([-0.05, 1.05])
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Precision-Recall Curve')
    plt.grid(True)
    plt.show()

import csv

with open("data_file.csv", "w", newline='') as f:
    w = csv.writer(f)
    _ = w.writerow(["precision", "recall"])
    w.writerows([
        [0.013, 0.951],
        [0.376, 0.851],
        [0.441, 0.839],
        [0.570, 0.758],
        [0.635, 0.674],
        [0.721, 0.604],
        [0.837, 0.531],
        [0.860, 0.453],
        [0.962, 0.348],
        [0.982, 0.273],
        [1.0, 0.0]
    ])

plot_data("data_file.csv")
