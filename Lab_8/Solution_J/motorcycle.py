from vehicle import Vehicle

class Motorcycle(Vehicle):
    def special_move(self, obs_loc):
        return super().special_move(obs_loc)
    
    def slow(self,obs_loc):
        return "slow overriden"