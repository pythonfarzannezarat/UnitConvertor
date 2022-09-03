class Commands:
    def __init__(self, entry_from, list_box_from, list_box_to):
        self.entryFrom = entry_from
        self.listBoxFrom = list_box_from
        self.listBoxTo = list_box_to

    def __millimeter(self):
        result = 0
        if self.listBoxTo == 'MilliMeter':
            result = self.entryFrom
        elif self.listBoxTo == 'CentiMeter':
            result = self.entryFrom / 10
        elif self.listBoxTo == 'Inch':
            result = self.entryFrom / 25.4
        elif self.listBoxTo == 'Feet':
            result = self.entryFrom / 304.8
        elif self.listBoxTo == 'Yard':
            result = self.entryFrom / 914.4
        elif self.listBoxTo == 'Meter':
            result = (self.entryFrom / 10) / 100
        elif self.listBoxTo == 'Mile':
            result = self.entryFrom / 1609344
        elif self.listBoxTo == 'KiloMeter':
            result = ((self.entryFrom / 10)/100)/1000
        return result

    def __centimeter(self):
        result = 0
        if self.listBoxTo == 'MilliMeter':
            result = self.entryFrom * 10
        elif self.listBoxTo == 'CentiMeter':
            result = self.entryFrom
        elif self.listBoxTo == 'Inch':
            result = self.entryFrom / 2.54
        elif self.listBoxTo == 'Feet':
            result = self.entryFrom / 30.48
        elif self.listBoxTo == 'Yard':
            result = self.entryFrom / 91.44
        elif self.listBoxTo == 'Meter':
            result = self.entryFrom / 100
        elif self.listBoxTo == 'Mile':
            result = self.entryFrom / 160934.4
        elif self.listBoxTo == 'KiloMeter':
            result = self.entryFrom/100000
        return result

    def units(self):
        if self.listBoxFrom == 'MilliMeter':
            return self.__millimeter()
        elif self.listBoxFrom == 'CentiMeter':
            return self.__centimeter()
