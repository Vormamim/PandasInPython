"""
Simple charting for weather data.
"""

import matplotlib.pyplot as plt


def plot_line(df, x_col, y_col, filename=None):
    """Plot a line chart. Save to file if filename provided, else show."""
    plt.figure()
    plt.plot(df[x_col], df[y_col])
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.grid(True)
    
    if filename:
        plt.savefig(filename)
        print(f"Saved to {filename}")
    else:
        plt.show()
