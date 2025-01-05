class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        return f'{self.__hours:02}:{self.__minutes:02}:{self.__seconds:02}'
    
    def next_second(self):
        self.__seconds += 1
        if self.__seconds == 60:
            self.__seconds = 0
            self.__minutes += 1
            if self.__minutes == 60:
                self.__minutes = 0
                self.__hours += 1
                if self.__hours == 24:
                    self.__hours = 0

    def prev_second(self):
        self.__seconds -= 1
        if self.__seconds < 0:
            self.__seconds = 59
            self.__minutes -= 1
            if self.__minutes < 0:
                self.__minutes = 59
                self.__hours -= 1
                if self.__hours < 0:
                    self.__hours = 23

# Example usage
if __name__ == "__main__":
    timer = Timer(23, 59, 59)
    print(timer)  # Output: 23:59:59
    timer.next_second()
    print(timer)  # Output: 00:00:00
    timer.prev_second()
    print(timer)  # Output: 23:59:59