import re

row = 2000000
searcharea = 4000000

def dist_man(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def search_along_edges(sensors):
    for (sx, sy, sdist) in sensors:
        for border_x in range(max(0, sx - sdist - 1), min(searcharea, sx + sdist + 2)):
            for border_y in [sy + (sdist + 1 - abs(border_x - sx)), sy - (sdist + 1 - abs(border_x - sx))]:
                if 0 <= border_y <= searcharea:
                    for (sx1, sy1, d) in sensors:
                        if dist_man((border_x,border_y), (sx1, sy1)) <= d:
                            break
                    else:
                        return border_x, border_y

if __name__ == '__main__':
    input = open("day15.txt", "r").read().splitlines()
    valid_beacons = set()
    invalid_sensors = set()
    sensors = set()
    for line in input:
        sensor_x, sensor_y, beacon_x, beacon_y = [int(v) for v in re.findall("(-?\d+)", line)]
        if beacon_y == row:
            valid_beacons.add((beacon_x, beacon_y))
        dist = dist_man((sensor_x, sensor_y), (beacon_x, beacon_y))
        if sensor_y - dist <= row <= sensor_y + dist:
            for x in range(sensor_x - dist + dist_man((0, sensor_y), (0, row)),
                           sensor_x + dist - dist_man((0, sensor_y), (0, row)) + 1):
                invalid_sensors.add(x)
        sensors.add((sensor_x, sensor_y, dist))

    sol1 = len(invalid_sensors) - len(valid_beacons)
    valid_x, valid_y = search_along_edges(sensors)
    print(sol1, valid_x * searcharea + valid_y)