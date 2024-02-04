# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):
        """Create a monitoring station."""

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    # done by Joe
    def typical_range_consistent(self):
        consistent = True
        try:
            # check for data availability
            consistent = consistent and (type(self.typical_range) == tuple)
            consistent = consistent and (len(self.typical_range) == 2)
            for i in self.typical_range:
                consistent = consistent and (type(i) == float)
            
            # check for data consistency
            
            consistent = consistent and (self.typical_range[1] >= self.typical_range[0])
        except:
            consistent = False
        return consistent

def inconsistent_typical_range_stations(stations):
    """given a list of station objects, return a list of station objects with inconsistent data"""

    faulty_stations = []
    for station in stations:
        if not station.typical_range_consistent():
            faulty_stations.append(station)
    
    return faulty_stations