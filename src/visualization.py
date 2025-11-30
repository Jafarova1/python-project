import matplotlib.pyplot as plt
import matplotlib.ticker as ticker # Imported to control axis labels for integer values
import numpy as np

def plot_movie_years(movies):
    # Extract only the release years (ensuring they are numbers)
    years = [
        m["year"] 
        for m in movies 
        if isinstance(m.get("year"), (int, float)) # Filters out None or non-numeric years
    ]

    # Set up the figure size
    fig, ax = plt.subplots(figsize=(8, 5))

    if not years:
        # Display a message if no movie year data is available
        ax.text(0.5, 0.5, 'No movie year data available for the histogram.', 
                ha='center', va='center', fontsize=12, color='gray')
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_title("Movie Release Years Histogram")
        return fig

    # Dynamic Bin Calculation: Creates one bin per year in the data range
    year_range = max(years) - min(years) if years and max(years) > min(years) else 0
    # Use the range + 1 as the number of bins
    num_bins = int(year_range + 1) if year_range > 0 else 10
    
    # Plot the histogram
    ax.hist(years, 
            bins=num_bins, 
            edgecolor='black', 
            color='#1f77b4', # A clean, professional blue color
            alpha=0.8)

    # Set titles and labels for clarity
    ax.set_xlabel("Release Year", fontsize=12)
    ax.set_ylabel("Number of Movies", fontsize=12)
    ax.set_title("Distribution of Movie Release Years (Current Quiz)", fontsize=14)
    
    # --- FIXES: Ensure Integer Ticks ---
    
    # 1. Force X-axis labels to display as integers (removes .0 and .5 labels)
    ax.xaxis.set_major_locator(ticker.MaxNLocator(integer=True)) 
    
    # 2. Force Y-axis labels to display as integers (removes 0.5, 1.5, etc.)
    ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True)) 
    
    # Adjust Y-limit slightly to prevent bars from touching the top edge
    ax.set_ylim(bottom=0, top=ax.get_ylim()[1] + 0.5)

    # Rotate X-axis labels for better readability, especially with many years
    plt.xticks(rotation=45, ha='right')
    ax.grid(axis='y', alpha=0.5, linestyle='--') # Add horizontal grid lines for easier counting
    plt.tight_layout() # Ensures all plot elements fit nicely

    return fig