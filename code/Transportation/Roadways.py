from Transportation import Transportation

class Roadway():
    #Roadways Section

        def __init_(self, l, s):
            self.lanes = l
            self.sensor = s

class Lanes():
    # Lanes Section

    def __init_(self, t, lo, sz, o, n):
        self.type = t
        self.location = lo
        self.size = sz
        self.occupancy = o
        self.number = n


class Sensors():
    # Sensors Section

    def __init_(self, t, lo, sz, na):
        self.type = t
        self.location = lo
        self.size = sz
        self.name = na