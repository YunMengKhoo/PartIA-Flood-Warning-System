# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine
from .station import MonitoringStation
def stations_by_distance(stations, p):
    station_distance_list = []
    for station in stations:
        distance = haversine(station.coord, p)
        station_distance_list.append((station,distance))
    return sorted_by_key(station_distance_list, 1)

def testing_stations_by_distance():
    station1 = MonitoringStation(1,101,'station 1', (5,5),(0,10),'river 1', 'town 1')
    station2 = MonitoringStation(2,102,'station 2', (90,90),(0,10),'river 2', 'town 2')
    p = (5,5)
    stations = [station1, station2]
    assert stations_by_distance(stations, p)[0][0] == station1, "Testing failed for stations_by_distance"

# done by Joe
def stations_within_radius(stations, centre, r):
    """given a list of station objects, a coordinate for the centre, and radius, return stations within radius of the centre"""
    result = []
    for station in stations:
        if haversine(station.coord,centre) <= r:
            result.append(station)
    
    return result


def testing_stations_within_radius():
    station1 = MonitoringStation(1,101,'station 1', (5,5),(0,10),'river 1', 'town 1')
    station2 = MonitoringStation(2,102,'station 2', (90,90),(0,10),'river 2', 'town 2')
    centre = (5,5)
    r = 5
    stations = [station1, station2]

    assert stations_within_radius(stations, centre, r) == [station1], "Testing failed for stations_within_radius"
    
    # done by Joe
def rivers_with_station(stations):
    """given a list of station objects, return a set of all rivers that have stations"""
    rivers = set()
    for station in stations:
        rivers.add(station.river)
    
    return rivers

def testing_rivers_with_station():
    station1 = MonitoringStation(1,101,'station 1', (5,5),(0,10),'river 1', 'town 1')
    station2 = MonitoringStation(2,102,'station 2', (90,90),(0,10),'river 2', 'town 2')
    stations = [station1, station2]

    assert rivers_with_station(stations) == {'river 1', 'river 2'}, "Testing failed for rivers_with_stations"

def stations_by_river(stations):
    """given a list of all station objects, return a dictionary with river names as the key and corresponding station objects as values"""
    result = {}
    for station in stations:
        if station.river not in result:
            result[station.river] = [station]
        else:
            result[station.river].append(station)
    
    return result

def testing_stations_by_river():
    station1 = MonitoringStation(1,101,'station 1', (5,5),(0,10),'river 1', 'town 1')
    station2 = MonitoringStation(2,102,'station 2', (90,90),(0,10),'river 2', 'town 2')
    stations = [station1, station2]
    assert stations_by_river(stations) == {'river 1': [station1], 'river 2': [station2]}, "Testing failed for stations_by_river"


#Can we count number of values in key
#reate list of tuples( river, numberx) wher numberx is number of values
def rivers_by_station_number(stations, N):
    """given a list of all station objects (which are station + corresponding details and data), we want to get a list of N rivers and the corresponding number of monitoring stations with the highest number of strings"""
    """From this list, it should be sorted by number of stations from largest to smallest. In the case of ties, all involved rivers are included"""
    riverdict = stations_by_river(stations)
    river_number_list = []
    for river in riverdict:
        
        numberx = len(riverdict[river])
        river_number_list.append((river,numberx))

    river_number_list = sorted_by_key(river_number_list, 1)
    river_number_list.reverse()
    while river_number_list[N][1] == river_number_list[N-1][1] and N <= len(river_number_list):
        N += 1
    return river_number_list[:N]

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
