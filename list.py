red = Line("red", ["North Springs", "Sandy Springs", "Dunwoody", "Medical Center"
, "Buckhead", "Art Center", "Midtown", "North Avenue", "Civic Center",
"Peachtree Center", "Five Points", "Garnett", "Oakland City",
"Lakewood", "East Point", "College Park", "Airpirt"])

gold = Line("gold", ["Doravile", "Chamblee", "Brookhaven", "Oglethorpe",
"Lenox", "Lindberghh Center", "Art Center", "Midtown", "North Avenue",
"Civic Center", "Peachtree Center", "Five Points", "Garnett",
"Oakland City", "Lakewood", "East Point", "College Park", "Airpirt"])

blue = Line("blue", ["Indian Creek", "Kensington", "Avondale", "Decatur",
"East Lake", "Edgewood", "Candler Park", "Inman Park", "Reynoldstown",
"King Memorial", "Georgia State", "Five Points", "Dome",
"Philips Areana", "CNN Center", "Vine City", "Ashby", "West Lake",
"Hamilton E. Holmes"])

green = Line("green", ["Edgewood", "Candler Park", "Inman Park", "Reynoldstown",
"King Memorial", "Georgia State", "Five Points", "Dome",
"Philips Areana", "CNN Center", "Vine City", "Ashby", "Bankhead"])

class Line:
    """A MARTA line of stations"""

    def __init__(self, name, stations):
        self.name = name
        self.stations = stations

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
