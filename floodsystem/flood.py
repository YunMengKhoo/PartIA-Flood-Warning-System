from .utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    """given a list of station objects and the thershold tol, return a list of tuples containing station objects with relative level over tol, and their relative levels, sorted in descending order by relative level"""
    stations_over_thresh = []
    for station in stations:
        if station.relative_water_level() is not None:
            
            if station.relative_water_level() > tol:
                stations_over_thresh.append((station,station.relative_water_level()))
    stations_over_thresh = sorted_by_key(stations_over_thresh,1,reverse=True)
    return stations_over_thresh