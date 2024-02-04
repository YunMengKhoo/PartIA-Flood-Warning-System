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


#done by Joe
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
            result[station.river] = station
        else:
            result[station.river].append(station)
    
    return result