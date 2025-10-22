"""
This is door class interface that passes all the methods through each subclass of door

"""

import abc


class Door(abc.ABC):
    @abc.abstractmethod
    def examine_door(self):
        pass

    @abc.abstractmethod
    def menu_options(self):
        pass
    
    @abc.abstractmethod
    def get_menu_max(self):
        pass
    
    @abc.abstractmethod
    def attempts(self, option):
        pass
    
    @abc.abstractmethod
    def is_unlocked(self):
        pass
    
    @abc.abstractmethod
    def clue(self):
        pass
    
    @abc.abstractmethod
    def success(self):
        pass
    
    