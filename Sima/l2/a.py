class Time():
    def __init__(self, h, m, s, mm):
        self.hours = h
        self.minutes = m
        self.seconds = s
        self.microseconds = mm

    def __add__(self, other):
        m = self.minutes + other.minutes
        h = self.hours + other.hours
        s = self.seconds + other.seconds
        mm = self.microseconds + other.microseconds
        while(mm > 1000):
            mm -= 1000
            s += 1
        while(s >= 60):
            s -= 60
            m += 1
        while(m >= 60):
            m -= 60
            h += 1

        return Time(h, m, s, mm)

    def __str__(self):
        return f"Hours: {self.hours}, minutes: {self.minutes}, seconds: {self.seconds}, microseconds: {self.microseconds}"


t = Time(0, 0, 0, 0)
n = int(input("Enter the number of inputs:"))
for i in range(n):
    # h, m, s, mm = map(int, input(f"Enter {i+1} numbers: ").split())
    h, m, s, mm = map(int, input().split())
    t += Time(h, m, s, mm)


print(t)
