
class Task():
    def __init__(self, desc, date, time):
        self._desc = desc
        self._date = date
        self._time = time
    
    @property
    def date(self):
        return self._date

    def __str__(self):
        return f"{self._desc} -- Due: {self._date} at {self._time}"
    
    def __repr__(self):
        return f"{self._desc},{self._date},{self._time}"
    
    def __lt__(self, other):
        
        task1 = [int(self._date.replace("/", "")), int(self._time.replace(":", "")), self._desc]
        task2 = [int(other._date.replace("/", "")), int(other._time.replace(":", "")), other._desc]

        if task1 < task2:
            return True
        else:
            return False
        
    