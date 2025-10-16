import random as rand
from car import Car
from motorcycle import Motorcycle
from vehicle import Vehicle
from truck import Truck
import check_input
    
def main():
    lanes = 3
    track_length = 100
    track = [["-"*track_length]*lanes]
    obstacles = []
    
    vehicles = [Car("Lightning Car","C",7),Motorcycle("Swift Bike","M",6),Truck("Behemoth Truck","T",8)]
    vehicle_intials = ["C","M","T"]
    play = True
    print("Rad Racer!")
    print("Choose a Vehicle and race it down the track (player = ""P""). Slow down for obstacles (""0"") or else you'll crash!")
    print("""
1. Lightning Car - a fast car. Speed: 7. Special: Nitro Boost (1.5x speed)
2. Swift Bike - a speedy motorcycle. Speed: 8. Special Wheelie (2x speed but there's a chance you'll wipe out)
3. Behemoth Truck - a heavy truck. Speed 6. Special: Ram (2x speed and it smashes through obstacles).
""")
    
    vehicle_choice = check_input.get_int_range("Choose your vehicle (1-3): ",1,3)
    player_index = vehicle_choice - 1
    vehicle_intials[player_index] = "P"
    player = vehicles[player_index]

    while play:
        print()
        for vehicle in vehicles:
            print(str(vehicle))

        for r, row in enumerate(track):
            for v,value in enumerate(row):
                print(value, end = "")

                print()
        action_choice = check_input.get_int_range("Choose action (1. Fast, 2. Slow, 3. Special Move): ",1,3)

        match action_choice:
            case 1:
                print(player.fast(3))
            case 2:
                print(player.slow(3))
            case 3:
                print(player.special_move(3))

        for i, vehicle in enumerate(vehicles):

            if i == player_index:
                continue

            prob = rand.random()

            if prob < 0.30:
                print(vehicle.fast(3))
            elif prob < 0.60:
                print(vehicle.special_move(3))
            else:
                print(vehicle.slow(3))

        
            
        

if __name__ == "__main__":
    main()