from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river

def run():
    """Requirements for Task 1A"""

    stations = build_station_list()
    N = 10
    most_monitored_rivers = rivers_by_station_number(stations, N)
    print("The most monitored rivers and their respective number of monitoring stations are", most_monitored_rivers)

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()