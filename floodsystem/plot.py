import matplotlib.pyplot as plt
import matplotlib
from .analysis import polyfit
def plot_water_levels(station, dates, levels):
    """given a station object, a set of dates and its water levels during these dates, returns a plot of water levels against dates, with labelling"""

    plt.plot(dates,levels)

    low, high = station.typical_range
    plt.axhline(y=low, color='r', linestyle='-', label='typical low')
    plt.axhline(y=high, color='r', linestyle='-', label='typical high')


    plt.xlabel("Date")
    plt.ylabel("Water level (m)")

    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.tight_layout()

    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    """given a station objects, dates and levels, and the degree of a polynomial fit, plot the polynomial fit with the water levels"""

    plt.plot(dates, levels, label="Water levels")

    poly, d0 = polyfit(dates,levels,p)

    x = matplotlib.dates.date2num(dates)

    plt.plot(x, poly(x-d0), label=(f"{p} degree polynomial fit"))

    plt.title(station.name)
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.legend()
    
    plt.show()
