from datetime import datetime
from pytz import timezone

class Direction(Enum):
    North = 1
    South = 2
    East = 3
    West = 4

def findRoute(origin, dest):
    return findRouteHelper(origin, dest, [])

def findRouteHelper(origin, dest, route):
    origin_lines = findLinesWithStation(origin)
    dest_lines = findLinesWithStation(dest)
    intersects = origin_lines.intersection(dest_lines)
    print(intersects)
    route = []
    if len(intersects) >= 1:
        route.append({
            lines: intersects,
            direction: findDirection(origin, dest, min(intersects))
        })
        return route
    elif len(intersects) == 0:
        dest_line_name = min(dest_lines).name
        transfer = min(origin_lines).transfers[dest_line_name]
        route.append({
            lines: origin_lines,
            direction: findDirection(origin, transfer, min(intersects))
        })
        return findRouteHelper(transfer, dest, route)

def findLinesWithStation(station):
    lines = set()
    now_utc = datetime.now(timezone('UTC'))
    now_eastern = now_utc.astimezone(timezone('US/Eastern'))
    if now_eastern.hour < 5 and
       now_eastern.hour > 1 and
       now_eastern.minute > 30:
        return lines
    if station in red:
        if now_eastern.hour > 21
            lines.add(red_night)
        else:
            lines.add(red)
    if station in gold:
        lines.add(gold)
    if station in green:
        if now_eastern.hour > 21
            lines.add(green_night)
        else:
            lines.add(green)
    if station in blue:
        lines.add(blue)
    return lines

def findDirection(origin, dest, line):
    if line.name is 'red' or line.name is 'gold':
        if line.index(origin) < line.index(dest):
            return Direction.North
        else:
            return Direction.South
    else:
        if line.index(origin) < line.index(dest):
            return Direction.East
        else:
            return Direction.West
