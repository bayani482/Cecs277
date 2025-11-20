"""
this class manages a list of tasks

"""

from task import Task


class TaskList:
    def __init__(self):
        """
        initializes the tasklist from the file into a list and sorts it
        
        """
        self._tasklist = []
        with open('tasklist.txt', 'r', newline='') as file:
            for line in file:
                    parts = line.strip().split(",")
                    if len(parts) == 3:
                        desc, date, time = parts
                        self._tasklist.append(Task(desc, date, time))
        self._tasklist.sort()

    def add_task(self, desc, date, time):
        """
        adds a task to the tasklist and sorts it

        Args:
            desc (str): string description of the task
            date (str): string date in MM/DD/YYYY format
            time (str): string time in HH:MM AM/PM format
        """
        self._tasklist.append(Task(desc, date, time))
        self._tasklist.sort()

    
    def get_current_task(self):
        """
        gets the current task in the tasklist

        Returns:
            tuple: description, date, time of the current task
        """
        if len(self._tasklist) == 0:
            return None
        return self._tasklist[0]
    
    def mark_complete(self):
        """
        marks the current task as complete by removing it from the tasklist

        Returns:
            tuple: description, date, time of the completed task
        """
        if len(self._tasklist) == 0:
            return None
        return self._tasklist.pop(0)
    
    def save_file(self):
        """
        saves the tasklist to the file
        """
        with open('tasklist.txt', 'w') as file:
            for x in self._tasklist:
                file.write(repr(x) + '\n')
    
    def __len__(self):
        """
        gets the length of the tasklist

        Returns:
            int: length of the tasklist
        """
        return len(self._tasklist)
    
    def __iter__(self):
        """
        initializes the iterator

        Returns:
            int: the iterator object
        """
        self._n = 0
        return self
    
    def __next__(self):
        """
        gets the next task in the tasklist
        Raises:
            StopIteration: if there are no more tasks

        Returns:
            Task: the next task in the tasklist
        """
        if self._n >= len(self._tasklist):
            raise StopIteration
        self._n += 1
        return self._tasklist[self._n-1]