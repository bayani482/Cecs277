"""
this class represents a task with description, date, and time

"""

class Task:
    def __init__(self, desc, date, time):
        """
        initialize a Task object

        Args:
            desc (str): description of the task
            date (str): date in MM/DD/YYYY format
            time (str): time in HH:MM AM/PM format
        """
        self._desc = desc
        self._date = date
        self._time = time
    @property
    def date(self):
        """
        getter for date
        Returns:
            str: date of the task
        """
        return self._date
    def __str__(self):
        """
        string representation of the task
        Returns:
            str: string formated in description - date at time
        """
        return f"{self._desc} - {self._date} at {self._time}"
    def __repr__(self):
        """
        string representation that gets saved to file
        Returns:
            str: string formated in description, date, time
        """
        return f"{self._desc},{self._date},{self._time}"
    def __lt__(self, other):
        """
        this compares two dates and times to see which is earlier and returns a boolean

        Args:
            other (_type_): _description_

        Returns:
            bool: true or false
        """
        month1, day1, year1 = self._date.split("/")
        month2, day2, year2 = other._date.split("/")
        hour1, min1 = self._time.split(":")
        hour2, min2 = other._time.split(":")
        self_key = (int(year1), int(month1), int(day1), int(hour1), int(min1), self._desc)
        other_key = (int(year2), int(month2), int(day2), int(hour2), int(min2), other._desc)
        
        return self_key < other_key