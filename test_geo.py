from floodsystem.geo import stations_by_distance, stations_within_radius, stations_by_river, rivers_with_station, rivers_by_station_number
from floodsystem.station import MonitoringStation

def testing_stations_by_distance():
    station1 = MonitoringStation(1,101,'station 1', (5,5),(0,10),'river 1', 'town 1')
    station2 = MonitoringStation(2,102,'station 2', (90,90),(0,10),'river 2', 'town 2')
    p = (5,5)
    stations = [station1, station2]
    assert stations_by_distance(stations, p)[0][0] == station1, "Testing failed for stations_by_distance"


def testing_stations_within_radius():
    station1 = MonitoringStation(1,101,'station 1', (5,5),(0,10),'river 1', 'town 1')
    station2 = MonitoringStation(2,102,'station 2', (90,90),(0,10),'river 2', 'town 2')
    centre = (5,5)
    r = 5
    stations = [station1, station2]

    assert stations_within_radius(stations, centre, r) == [station1], "Testing failed for stations_within_radius"

def testing_rivers_with_station():
    station1 = MonitoringStation(1,101,'station 1', (5,5),(0,10),'river 1', 'town 1')
    station2 = MonitoringStation(2,102,'station 2', (90,90),(0,10),'river 2', 'town 2')
    stations = [station1, station2]

    assert rivers_with_station(stations) == {'river 1', 'river 2'}, "Testing failed for rivers_with_stations"


def testing_stations_by_river():
    station1 = MonitoringStation(1,101,'station 1', (5,5),(0,10),'river 1', 'town 1')
    station2 = MonitoringStation(2,102,'station 2', (90,90),(0,10),'river 2', 'town 2')
    stations = [station1, station2]
    assert stations_by_river(stations) == {'river 1': [station1], 'river 2': [station2]}, "Testing failed for stations_by_river"

def testing_rivers_by_station_number():
    station1 = MonitoringStation(1,101,'station 1', (5,5),(0,10),'river 1', 'town 1')
    station2 = MonitoringStation(2,102,'station 2', (90,90),(0,10),'river 2', 'town 2')
    station3 = MonitoringStation(3,103,'station 3', (5,5),(0,10),'river 3', 'town 1')
    station4 = MonitoringStation(4,104,'station 4', (90,90),(0,10),'river 3', 'town 2')
    station5 = MonitoringStation(5,105,'station 5', (5,5),(0,10),'river 1', 'town 1')
    station6 = MonitoringStation(6,106,'station 6', (90,90),(0,10),'river 2', 'town 2')
    station7 = MonitoringStation(7,107,'station 7', (5,5),(0,10),'river 1', 'town 1')
    station8 = MonitoringStation(8,108,'station 8', (90,90),(0,10),'river 2', 'town 2')
    stations = [station1, station2,station3,station4,station5,station6,station7,station8]
    N=1
    assert set(rivers_by_station_number(stations,N)) == {('river 1', 3), ('river 2', 3)}, "Testing failed for rivers_by_station_number"
