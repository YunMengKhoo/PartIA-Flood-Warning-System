import matplotlib.pyplot as plt

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