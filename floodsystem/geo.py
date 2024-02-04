# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine
def stations_by_distance(stations, p):
    station_distance_list = []
    for station in stations:
        distance = haversine(station.coord, p)
        station_distance_list.append((station,distance))
    return sorted_by_key(station_distance_list, 1)


# done by Joe
def stations_within_radius(stations, centre, r):
    """given a list of station objects, a coordinate for the centre, and radius, return stations within radius of the centre"""
    result = []
    for station in stations:
        if haversine(station.coord,centre) <= r:
            result.append(station)
    
    return result

# done by Joe
def rivers_with_station(stations):
    """given a list of station objects, return a set of all rivers that have stations"""
    rivers = set()
    for station in stations:
        rivers.add(station.river)
    
    return rivers

def stations_by_river(stations):
    """given a list of all station objects, return a dictionary with river names as the key and corresponding station objects as values"""
    result = {}
    for station in stations:
        if station.river not in result:
            result[station.river] = [station]
        else:
            result[station.river].append(station)
    
    return result


#Can we count number of values in key
#reate list of tuples( river, numberx) wher numberx is number of values
def rivers_by_station_number(stations, N):
    """given a list of all station objects (which are station + corresponding details and data), we want to get a list of N rivers and the corresponding number of monitoring stations with the highest nuber of strings"""
    """From this list, it should be sorted by number of stations from largest to smallest. In the case of ties, all involved rivers are included"""
    riverdict = stations_by_river(stations)
    river_number_list = []
    for station in stations:
        
        numberx = len(riverdict[station.river])
        river_number_list.append((station.river,numberx))

    river_number_list = sorted_by_key(river_number_list, 1).reverse()
    
    while river_number_list[N][1] == river_number_list[N-1][1] and N <= len(river_number_list):
        N += 1
    return sorted_by_key(river_number_list[:N])
