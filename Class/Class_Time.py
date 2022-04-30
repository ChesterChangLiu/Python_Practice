class Time:      
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)    # 2 digit integers
    def __add__(self, other):     
        seconds = self.second + other.second
        t = Time()
        t.hour = self.hour
        t.minute = self.minute
        if seconds > 60:
           t.second = seconds - 60
           t.minute = self.minute + 1
        else:
           t.second = seconds
        return t
start=Time(9, 45)
print(start)               # this print is using the method __str__()
duration = Time(0, 0, 75)  # due to the coding of add() the maximum allowed duration is 119 seconds
print(start+duration)      # this line is executed using the method __add__()
