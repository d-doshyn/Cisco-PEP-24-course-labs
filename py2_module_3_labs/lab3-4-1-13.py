class WeekDayError(Exception):
    pass
	

class Weeker:
    right_days_arr = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    def __init__(self, day):
        if day not in self.right_days_arr:
            raise WeekDayError

        self.__day = day

    def __str__(self):
        return self.__day

    def add_days(self, n):
        iter_count = 0
        day_ind = self.right_days_arr.index(self.__day)

        while iter_count <= n + 1:
            day_ind += 1

            if day_ind == 7:
                day_ind = 0

            iter_count += 1

        self.__day = self.right_days_arr[day_ind]

    def subtract_days(self, n):
        iter_count = 0
        day_ind = self.right_days_arr.index(self.__day)

        while iter_count <= n + 1:
            day_ind -= 1

            if day_ind == -1:
                day_ind = 6

            iter_count += 1

        self.__day = self.right_days_arr[day_ind]


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")