import datetime

class Schedule:
    def __init__(self, month, day, hour, minute):
        self.dateSched = datetime.date(2021, month, day)
        self.timeSched = datetime.time(hour, minute, 0)