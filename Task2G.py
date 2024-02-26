import datetime
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.flood import stations_level_over_threshold

# we note that for thames, typical high is equal to alert level (7) whihc is a good reference point
#Historic highest is 7.41 which is in 2003
# low is 6.58, warning level is 7.10.
# So let low be tol=0.8, tol=1 be moderate, tol= 1.1 be high,tol=1.2 be severe.

def run():
    """Requirements for Task 2G"""

    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)

    tol = 0.8 
    stations_over_thresh = stations_level_over_threshold(stations,tol)

    for i in stations_over_thresh:
        print("Low risk", i[0].name,i[1])

    tol = 1.0
    stations_over_thresh = stations_level_over_threshold(stations,tol)

    for i in stations_over_thresh:
        print("Moderate risk", i[0].name,i[1])

    tol = 1.1
    stations_over_thresh = stations_level_over_threshold(stations,tol)

    for i in stations_over_thresh:
        print("High risk", i[0].name,i[1])

    tol = 1.2
    stations_over_thresh = stations_level_over_threshold(stations,tol)

    for i in stations_over_thresh:
        print("Severe risk", i[0].name,i[1])

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()
    
