import matplotlib.pyplot as plt
import numpy as np

def plot_movie_years(movies):
    years = [m["year"] for m in movies if m["year"] is not None]
    fig, ax = plt.subplots()
    ax.hist(years, bins=10, color="skyblue")
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of Movies")
    ax.set_title("Movie Release Years Histogram")
    return fig