import datetime
import calendar

class Schedule:
    def __init__(self, userDate, userTime):
        self.dateSched = datetime.datetime.strptime(userDate + " 2021", "%B %d %Y")
        self.timeSched = datetime.datetime.strptime(userTime, "%I:%M %p")
        self.wholeDateTime = datetime.datetime.strptime(userDate + " 2021 " + userTime, "%B %d %Y %I:%M %p")
        self.inMonth = self.dateSched.strftime("%B")
        self.inDay = self.dateSched.strftime("%d")
        self.dayName = calendar.day_name[self.dateSched.weekday()]
        self.inTime = self.timeSched.strftime("%H:%M")
        self.inTimeMin = self.timeSched.strftime("%M")

    def __str__(self):
        return 'The scheduled date is on {self.inMonth} {self.inDay}, {self.dayName}, at {self.inTime}'.format(self = self)