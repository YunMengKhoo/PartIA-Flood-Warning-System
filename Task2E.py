import datetime
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels

def run():
    """Requirements for Task 2E"""

    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    
    N = 5
    dt = 10
    stations_at_risk = stations_highest_rel_level(stations,N)
    for station in stations_at_risk:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        plot_water_levels(station,dates,levels)
    



if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
