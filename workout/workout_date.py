import datetime

class Workout_Date:

    def __init__(self):

        self.d = {}
        self.week = int(input("몇 주차인지 입력 바랍니다: "))
        date = input("yyyymmdd(8): ")
        year = int(date[0:4])
        month = int(date[4:6])
        day = int(date[6:])



        self.d['{}-{}-{}, 화요일'.format(year, month, day + 7 * (self.week - 1))] = 0
        self.d['{}-{}-{}, 목요일'.format(year, month, day + 2 + 7 * (self.week - 1))] = 0
        self.d['{}-{}-{}, 토요일'.format(year, month, day + 4 + 7 * (self.week - 1))] = 0



    def getDate(self):
        return self.d

    def getWeek(self):
        return self.week
