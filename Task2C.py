from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    """Requirements for Task 2B"""

    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    
    N = 10
    stations_at_risk = stations_highest_rel_level(stations,N)
    for station in stations_at_risk:
        print(station.name, station.relative_water_level())


if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()
