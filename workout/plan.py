import barbell_row, squat, deadlift, oh_press, bench_press, workout_date

class Plan:

    def __init__(self):

        self.date = workout_date.Workout_Date()
        self.week = self.date.getWeek()-1
        self.d = self.date.getDate()
        self.squat = squat.Squat().getTm()
        self.deadlift = deadlift.Deadlift().getTm()
        self.barbell_row = barbell_row.Barbell_Row().getTm()
        self.oh_press = oh_press.Oh_Press().getTm()
        self.bench_press = bench_press.Bench_Press().getTm()


    def planMaker(self):

        l = self.d.keys()
        t = 0

        for i in l:

            s = []
            if t%2 !=1:
                s.append("A Set {}, {}, {}".format("squat", "bench_press", "barbell_row"))
                s.append(self.squat//2+2.5*t)
                s.append(self.bench_press//2+2.5*t)
                s.append(self.barbell_row//2+2.5*t)
            else:
                s.append("B Set {}, {}, {}".format("squat", "oh_press", "deadlift"))
                s.append(self.squat//2 + 2.5 * t)
                s.append(self.oh_press//2 + 2.5 * t)
                s.append(self.deadlift//2 + 2.5 * t)
            t+=1
            self.d[i] = s


    def getPlan(self):
        self.planMaker()
        print(self.d)
        return


p = Plan()
p.getPlan()