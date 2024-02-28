from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level
from Task2G import run
def test_2G():
    station1 = MonitoringStation(1,101,'station 1', (5,5),(0.0,10.0),'river 1', 'town 1')
    station2 = MonitoringStation(2,102,'station 2', (90,90),(0.0,10.0),'river 2', 'town 2')
    station3 = MonitoringStation(3,103,'station 3', (5,5),(0.0,10.0),'river 3', 'town 1')
    station4 = MonitoringStation(4,104,'station 4', (90,90),(0.0,10.0),'river 3', 'town 2')
    station5 = MonitoringStation(5,105,'station 5', (5,5),(0.0,10.0),'river 1', 'town 1')
    station1.latest_level = 10
    station2.latest_level = 8
    station3.latest_level = 9
    station4.latest_level = 11.5
    station5.latest_level = 100

    stations = [station1, station2, station3, station4, station5]

    

    assert run(stations) == [[station5],[station4],[],[station1,station3]], "Task2G error"