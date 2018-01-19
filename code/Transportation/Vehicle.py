class Vehicle:
    #Vehicle Section

        def __init_(self, t, m, sz, sp, co, w, do, se, li):
            self.type = t
            self.model = m
            self.size = sz
            self.speed = sp
            self.color = co
            self.wheels = w
            self.doors = do
            self.seats = se
            self.lights = li


class Autonmous(type):
    # Autonomous Vehicle Section

    def __init_(self, pa, t, m, sz, sp, co, w, do, se, li):
          self.passengers = pa
            self.type = t
            self.model = m
            self.size = sz
            self.speed = sp
            self.color = co
            self.wheels = w
            self.doors = do
            self.seats = se
            self.lights = li

class Manual(type):
    # Manual Vehicles Section

    def __init_(self, dr, ft, pa, t, m, sz, sp, co, w, do, se, li):
        self.driver = dr
        self.fueltype = ft
        self.passengers = pa
        self.type = t
        self.model = m
        self.size = sz
        self.speed = sp
        self.color = co
        self.wheels = w
        self.doors = do
        self.seats = se
        self.lights = li