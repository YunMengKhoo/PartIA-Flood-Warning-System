from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
    city_centre = (52.2053, 0.1218)
    close_stations = stations_within_radius(stations,city_centre,10)
    print(sorted([station.name for station in close_stations]))
    

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
