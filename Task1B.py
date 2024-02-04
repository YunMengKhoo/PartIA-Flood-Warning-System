# take the algorithim done to calculate distance in task 1B from geo.py
from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 1B"""

    # Print the list of tuples involving the station name and its distance. 
    stations = build_station_list()
    p = (52.2053, 0.1218)
    # obtain all station data (stations is not equal to name of station)
    distance_oriented_station_list = stations_by_distance(stations,p)
    station_name_town_distance=[(x[0].name, x[0].town, x[1]) for x in distance_oriented_station_list]
    print("The 10 closest stations and their corresponding distances are", station_name_town_distance[:10])
    print("The 10 furthest stations and their corresponding distances are", station_name_town_distance[-10:])


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
