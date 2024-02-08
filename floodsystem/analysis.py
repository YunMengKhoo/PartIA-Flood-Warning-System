import numpy as np
import matplotlib

def polyfit(dates, levels, p):
    """given the water level time history (dates, levels) for a station and the degree of the polynomial, returns a polynomial fit object and axis shift """
    x = matplotlib.dates.date2num(dates)

    p_coeff = np.polyfit(x-x[0], levels, p)
    poly = np.poly1d(p_coeff)

    return poly, x[0]