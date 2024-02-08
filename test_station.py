# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def testing_inconsistent_typical_range_stations():
    station1 = MonitoringStation(1,101,'station 1', (5,5), (0.0,10.0), 'river 1', 'town 1')
    faulty_station1 = MonitoringStation(2,102,'station 2', (5,5), (10.0,0.0), 'river 2', 'town 2')
    faulty_station2 = MonitoringStation(3,103,'station 3', (5,5), None, 'river 3', 'town 3')
    faulty_station3 = MonitoringStation(4,104,'station 4', (5,5), 'faulty data', 'river 4', 'town 4')

    stations = [station1, faulty_station1, faulty_station2, faulty_station3]

    assert set(inconsistent_typical_range_stations(stations)) == {faulty_station1,faulty_station2,faulty_station3}, "Testing failed for inconsistent_typical_range_stations"