import datetime
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit

def run():
    """Requirements for Task 2F"""

    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    
    N = 5
    dt = 2
    p = 4
    stations_at_risk = stations_highest_rel_level(stations,N)
    for station in stations_at_risk:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        plot_water_level_with_fit(station,dates,levels,p)
    



if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()
