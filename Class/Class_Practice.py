class Time:
    def __init__(self):
        self.hours = 0
        self.minutes = 0
time1 = Time()
time1.hours = 7
time1.minutes = 15
print('{} hours'.format(time1.hours), end=' ')
print('and {} minutes'.format(time1.minutes))