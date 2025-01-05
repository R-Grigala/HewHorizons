class WeekDayError(Exception):
    pass

class Weeker:
    _days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    def __init__(self, day):
        if day not in self._days:
            raise WeekDayError("Invalid day of the week")
        self.__current_day = day

    def __str__(self):
        return self.__current_day

    def add_days(self, n):
        current_index = self._days.index(self.__current_day)
        new_index = (current_index + n) % len(self._days)
        self.__current_day = self._days[new_index]

    def subtract_days(self, n):
        current_index = self._days.index(self.__current_day)
        new_index = (current_index - n) % len(self._days)
        self.__current_day = self._days[new_index]


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
