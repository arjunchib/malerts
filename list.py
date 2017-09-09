red =
Line(
    "red",
    ["North Springs", "Sandy Springs", "Dunwoody", "Medical Center", "Buckhead", "Lindbergh Center", "Art Center", "Midtown", "North Avenue", "Civic Center", "Peachtree Center", "Five Points", "Garnett", "Oakland City", "Lakewood", "East Point", "College Park", "Airport"],
    {
        gold: "Lindbergh Center",
        green: "Five Points",
        blue: "Five Points"
    }
)

red_night =
Line(
    "red",
    ["North Springs", "Sandy Springs", "Dunwoody", "Medical Center", "Buckhead", "Lindbergh Center"],
    {
        gold: "Lindbergh Center",
        green: "Lindbergh Center",
        blue: "Lindbergh Center"
    }
    night=True
)

gold =
Line(
    "gold",
    ["Doravile", "Chamblee", "Brookhaven/Oglethorpe", "Lenox", "Lindbergh Center", "Art Center", "Midtown", "North Avenue", "Civic Center", "Peachtree Center", "Five Points", "Garnett", "West End", "Oakland City", "Lakewood/Fort McPherson", "East Point", "College Park", "Airport"],
    {
        red: "Lindbergh Center",
        green: "Five Points",
        blue: "Five Points"
    }
)

blue =
Line("blue",
    ["Indian Creek", "Kensington", "Avondale", "Decatur", "East Lake", "Edgewood", "Candler Park", "Inman Park", "Reynoldstown", "King Memorial", "Georgia State", "Five Points", "Dome", "Philips Areana", "CNN Center", "Vine City", "Ashby", "West Lake", "Hamilton E. Holmes"],
    {
        red: "Five Points",
        gold: "Five Points"
        green: "Ashby"
    }
 )

green =
Line("green",
    ["Edgewood", "Candler Park", "Inman Park", "Reynoldstown", "King Memorial", "Georgia State", "Five Points", "Dome", "Philips Areana", "CNN Center", "Vine City", "Ashby", "Bankhead"],
    {
        red: "Five Points",
        gold: "Five Points"
        blue: "Ashby"
    }
)

green_night =
Line("green",
    ["Edgewood", "Candler Park", "Inman Park", "Reynoldstown", "King Memorial", "Georgia State", "Five Points", "Dome", "Philips Areana", "CNN Center", "Vine City", "Ashby", "Bankhead"],
    {
        red: "Vine City",
        gold: "Vine City"
        blue: "Vine City"
    }
    night=True
)

class Line:
    """A MARTA line of stations"""

    def __init__(self, name, stations, transfers=[], night=False):
        self.name = name
        self.stations = stations
        self.transfers = transfers
        self.night = night
