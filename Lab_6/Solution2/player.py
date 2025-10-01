from die import Die

class Player():
    def __init__(self):

        self._dice = [Die(),Die(),Die()]
        self._points = 0
    
    @property
    def value(self):
        return self.__points
    
    def roll_dice(self):
        for d in self._dice:
            d.roll()
        self._dice.sort()

    def has_pair(self):
        for i in range(1,len(self._dice)):
            if self._dice[i-1] == self._dice[i]:
                self._points += 1
                return True
        return False
            
    def has_three_of_a_kinda(self):
        if self._dice[0] == self._dice[1] == self._dice[0] == self._dice[2]:
            self._points += 3
            return True
        return False
        
    def has_series(self):
        for i in range(1,len(self._dice)):
            if self._dice[i] - self._dice[i-1] != 1:
                return False
        self._points += 2
        return True

    def __str__(self):
        s = "\n"
        for i, d in enumerate(self._dice):
            s += " |D" + str(i + 1) + " = " + str(d) + "|"
        return s