class Clock:
    def __init__(self, h, m, s):
        self.hour = h
        self.minute = m
        self.second = s
    
    def __str__(self): # should always return a string
        hour_str = str(self.hour)
        minute_str = str(self.minute)
        second_str = str(self.second)

        if len(hour_str) == 1:
            hour_str = "0" + hour_str
        if len(minute_str) == 1:
            minute_str = "0" + minute_str
        if len(second_str) == 1:
            second_str = "0" + second_str

        return hour_str + ":" + minute_str + ":" + second_str
    
    def tick(self):
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
            if self.minute == 60:
                self.minute = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0

# main
c1 = Clock(23, 59, 52)
for i in range(15):
    c1.tick()
    print(c1)