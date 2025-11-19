"""
this class manages a list of tasks

"""

from task import Task


class TaskList:
    def __init__(self):
        """
        
        
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
        """_summary_

        Args:
            desc (_type_): _description_
            date (_type_): _description_
            time (_type_): _description_
        """
        self._tasklist.append(Task(desc, date, time))
        self._tasklist.sort()

    
    def get_current_task(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        if len(self._tasklist) == 0:
            return None
        return self._tasklist[0]
    
    def mark_complete(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        if len(self._tasklist) == 0:
            return None
        return self._tasklist.pop(0)
    
    def save_file(self):
        """
        
        """
        with open('tasklist.txt', 'w') as file:
            for x in self._tasklist:
                file.write(repr(x) + '\n')
    
    def __len__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return len(self._tasklist)
    
    def __iter__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        self._n = 0
        return self
    
    def __next__(self):
        """_summary_

        Raises:
            StopIteration: _description_

        Returns:
            _type_: _description_
        """
        if self._n >= len(self._tasklist):
            raise StopIteration
        self._n += 1
        return self._tasklist[self._n-1]