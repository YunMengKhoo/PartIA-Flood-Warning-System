from floodsystem.geo import rivers_with_station, stations_by_river
from floodsystem.stationdata import build_station_list


def run():
    stations = build_station_list()
    rivers = rivers_with_station(stations)
    num = len(rivers)
    first_ten = sorted(rivers)[:10]
    print(f"{num} stations. First 10 - {first_ten}")

    riverdict = stations_by_river(stations)
    for river in ['River Aire','River Cam','River Thames']:
        print(sorted([station.name for station in riverdict[river]]))

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
