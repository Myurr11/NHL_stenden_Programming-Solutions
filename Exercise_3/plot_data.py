import os
import csv
import numpy as np
import matplotlib.pyplot as plt

def write_sample_data(csv_file_path: str):
    """
    Writes sample precision-recall data into a CSV file.
    
    :param csv_file_path: The CSV file to save the sample data.
    """
    # Check if the directory exists, if not, create it
    os.makedirs(os.path.dirname(csv_file_path), exist_ok=True)

    # Write sample data to the CSV file
    with open(csv_file_path, "w", newline="") as result_csv:
        csv_writer = csv.writer(result_csv)
        _ = csv_writer.writerow(["precision", "recall"])
        csv_writer.writerows([[0.013, 0.951],
                              [0.376, 0.851],
                              [0.441, 0.839],
                              [0.570, 0.758],
                              [0.635, 0.674],
                              [0.721, 0.604],
                              [0.837, 0.531],
                              [0.860, 0.453],
                              [0.962, 0.348],
                              [0.982, 0.273],
                              [1.0, 0.0]])

def plot_data(csv_file_path: str):
    """
    Plots the precision-recall curve based on data from a .csv file,
    where precision is on the y-axis and recall is on the x-axis.
    
    :param csv_file_path: The CSV file containing the data to plot.
    """
    # Load data from the CSV file
    results = np.loadtxt(csv_file_path, delimiter=',', skiprows=1)

    # Plot the precision-recall curve
    plt.plot(results[:, 1], results[:, 0])
    plt.ylim([-0.05, 1.05])
    plt.xlim([-0.05, 1.05])
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Precision-Recall Curve')
    plt.show()

# Example usage
csv_file_path = 'data/data_file.csv'

# Optionally, write sample data to the file (do this once)
write_sample_data(csv_file_path)

# Plot the precision-recall curve based on the data
plot_data(csv_file_path)
