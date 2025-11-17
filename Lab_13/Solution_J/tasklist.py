from task import Task

class Tasklist:
    def __init__(self):

        self._tasklist =  []
        with open("tasklist.txt", "r") as taskfile:
            for line in taskfile:
                line = line.strip()
                if line:
                    desc, date, time = line.split(",")
                    task = Task(desc, date, time)
                    self._tasklist.append(task)
        self._tasklist.sort()

    def add_task(self, desc, date, time):
        task = Task(desc, date, time)
        self._tasklist.append(task)
        self._tasklist.sort()

    def get_current_task(self):
        return self._tasklist[0]
    
    def mark_complete(self):
        self._tasklist.pop(0)
        return self._tasklist[0]

    def save_file(self):
        with open("tasklist.txt", "w") as taskfile:
            for task in self._tasklist:
                taskfile.write(repr(task) + "\n")
        
    def __len__(self):
        return len(self._tasklist)
    
    def __iter__(self):
        self._n = -1
        return self
    
    def __next__(self):
        self._n += 1
        if self._n >= len(self._tasklist):
            raise StopIteration
        else:
            return self._tasklist[self._n]
