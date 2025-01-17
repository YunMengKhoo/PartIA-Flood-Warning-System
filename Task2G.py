import datetime
from floodsystem.utils import sorted_by_key
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.flood import stations_level_over_threshold

# we note that for thames, typical high is equal to alert level (7) whihc is a good reference point
#Historic highest is 7.41 which is in 2003
# low is 6.58, warning level is 7.10.
# So let low be tol=0.8, tol=1 be moderate, tol= 1.1 be high,tol=1.2 be severe.


stations = build_station_list()
update_water_levels(stations)

def run(stations):
    """Requirements for Task 2G"""

    # Build list of stations
    
    listed_stations = []

    sev_risk_tol = 1.2
    stations_over_thresh = stations_level_over_threshold(stations,sev_risk_tol)
    sev_risk_stations = []
    for i in stations_over_thresh:
        print("Severe risk", i[0].name,i[1])
        sev_risk_stations.append(i[0])
    listed_stations += stations_over_thresh

    high_risk_tol = 1.1
    stations_over_thresh = stations_level_over_threshold(stations,high_risk_tol)
    high_risk_stations = []

    for i in stations_over_thresh:
        if i not in listed_stations:
            print("High risk", i[0].name,i[1])
            high_risk_stations.append(i[0])
            listed_stations.append(i)
    
    mod_risk_tol = 1.0
    stations_over_thresh = stations_level_over_threshold(stations,mod_risk_tol)
    mod_risk_stations = []
    for i in stations_over_thresh:
        if i not in listed_stations:
            print("Moderate risk", i[0].name,i[1])
            mod_risk_stations.append(i[0])
            listed_stations.append(i)
    
    low_risk_tol = 0.8 
    stations_over_thresh = stations_level_over_threshold(stations,low_risk_tol)
    low_risk_stations = []
    for i in stations_over_thresh:
        if i not in listed_stations:
            low_risk_stations.append(i[0])
            print("Low risk", i[0].name,i[1])

    return [sev_risk_stations,high_risk_stations,mod_risk_stations,low_risk_stations]


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run(stations)
    
