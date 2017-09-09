red =
Line(
    "red",
    ["North Springs", "Sandy Springs", "Dunwoody", "Medical Center", "Buckhead", "Lindbergh Center", "Arts Center", "Midtown", "North Avenue", "Civic Center", "Peachtree Center", "Five Points", "Garnett", "West End", "Oakland City", "Lakewood/Ft. McPherson", "East Point", "College Park", "Airport"],
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
    ["Doraville", "Chamblee", "Brookhaven/Oglethorpe", "Lenox", "Lindbergh Center", "Arts Center", "Midtown", "North Avenue", "Civic Center", "Peachtree Center", "Five Points", "Garnett", "West End", "Oakland City", "Lakewood/Ft. McPherson", "East Point", "College Park", "Airport"],
    {
        red: "Lindbergh Center",
        green: "Five Points",
        blue: "Five Points"
    }
)

blue =
Line("blue",
    ["Hamilton E. Holmes", "West Lake", "Ashby", "Vine City", "Dome/GWCC/Philips Arena/CNN Center", "Five Points", "Georgia State", "King Memorial", "Inman Park/Reynoldstown", "Edgewood/Candler Park", "East Lake", "Decatur", "Avondale", "Kensington", "Indian Creek"],
    {
        red: "Five Points",
        gold: "Five Points"
        green: "Ashby"
    }
 )

green =
Line("green",
    ["Bankhead", "Ashby", "Vine City", "Dome/GWCC/Philips Arena/CNN Center", "Five Points", "Georgia State", "King Memorial", "Inman Park/Reynoldstown", "Edgewood/Candler Park"],
    {
        red: "Five Points",
        gold: "Five Points"
        blue: "Ashby"
    }
)

green_night =
Line("green",
    ["Bankhead", "Ashby", "Vine City"],
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
