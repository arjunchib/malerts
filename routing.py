def findRoute(origin, dest):
    origin_lines = findLinesWithStation(origin)
    dest_lines = findLinesWithStation(dest)
    route = []
    if origin_lines == dest_lines:
        if len(origin_lines) == 1:
            route.append("Take the " + origin_lines[0].name + " line " + findDirection(origin, dest, origin_lines[0]) + "bound towards " + dest)

def findLinesWithStation(station):
    lines = []
    if station in red:
        lines.append(red)
    if station in gold:
        lines.append(gold)
    if station in green:
        lines.append(green)
    if station in blue:
        lines.append(blue)
    return lines

def findDirection(origin, dest, line):
    if line.name is 'red' or line.name is 'gold':
        if line.index(origin) < line.index(dest):
            return "North"
        else:
            return "South"
    else:
        if line.index(origin) < line.index(dest):
            return "East"
        else:
            return "West"
