import datetime
import calendar
'''
class Schedule:
    def __init__(self, month, day, hour, minute):
        self.dateSched = datetime.date(2021, month, day)
        self.timeSched = datetime.time(hour, minute, 0)

    def __str__(self):
        return 'The scheduled date is {self.dateSched.month} at {self.timeSched}'.format(self=self)

'''
class Schedule:
    def __init__(self, userDate, userTime):
        self.dateSched = datetime.datetime.strptime(userDate + " 2021", "%B %d %Y")
        self.timeSched = datetime.datetime.strptime(userTime, "%I:%M %p")
        self.inMonth = self.dateSched.strftime("%B")
        self.inDay = self.dateSched.strftime("%d")
        self.dayName = calendar.day_name[self.dateSched.weekday()]
        self.inTime = self.timeSched.strftime("%H:%M")

    def __str__(self):
        #return 'The scheduled date is on {self.month} {self.day}, {self.dayName} at {self.timeSched}'.format(self = self)
        return 'The scheduled date is on {self.inMonth} {self.inDay}, {self.dayName}, at {self.inTime}'.format(self = self)