

class Hit:
    def __init__(self, modulo, sensore, time_stamp):
        self.modulo    = modulo
        self.sensore   = sensore
        self.time_stamp = time_stamp
    def __lt__(self, other):
        if self.time_stamp != other.time_stamp:
             return self.time_stamp < other.time_stamp
        elif  self.modulo != other.modulo:
             return self.modulo < other.modulo
        elif  self.sensore != other.sensore:
             return self.sensore < other.sensore
        else:
            return 0

    def __gt__(self, other):
        if self.time_stamp != other.time_stamp:
             return self.time_stamp > other.time_stamp
        elif  self.modulo != other.modulo:
             return self.modulo > other.modulo
        elif  self.sensore != other.sensore:
             return self.sensore > other.sensore
    def __eq__(self, other) :
        return self.time_stamp == other.time_stamp
    def __sub__(self, other) :
        return self.time_stamp - other.time_stamp
