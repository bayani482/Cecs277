
import random as rand
from car import Car
from motorcycle import Motorcycle
from vehicle import Vehicle
from truck import Truck
import check_input

def display_track(track, vehicles):
    print("\nTrack:")
    for i, row in enumerate(track):
        print(''.join(row) + f"  {vehicles[i]}")
    print()

def find_next_obstacle(track, lane, pos):
    try:
        return track[lane].index('#', pos + 1)
    except ValueError:
        return 9999  # No obstacle ahead

def main():
    track_length = 100
    lanes = 3


    track = [["-"*track_length]*lanes]


    vehicles_names = ['Car','Truck','Motorcycle']
    vehicle_letters = ['C','T','M']
    vehicle_speeds = [7,8,6]
    winners = []
    vehicles = []

    
    # Prompt user to choose a vehicle
    print("Choose your vehicle:")
    for i, name in enumerate(vehicles_names):
        print(f"{i+1}. {name}")
    choice = check_input.get_int_range("Enter choice: ", 1, 3) - 1
    while len(winners) <= len(vehicles):
        print("play game")
    # Create vehicle objects
        for i in range(3):
            if vehicles_names[i] == 'Car':
                vehicles.append(Car(vehicles_names[i], vehicle_letters[i], vehicle_speeds[i]))
            elif vehicles_names[i] == 'Motorcycle':
                vehicles.append(Motorcycle(vehicles_names[i], vehicle_letters[i], vehicle_speeds[i]))
            else:
                vehicles.append(Truck(vehicles_names[i], vehicle_letters[i], vehicle_speeds[i]))  # Placeholder for Truck

        # Set the player's vehicle initial to 'P'
        vehicles[choice]._initial = 'P'
        # Create track and place vehicles at start

    for i, v in enumerate(vehicles):
        track[i][0] = v._initial

    places = [None, None, None]

    while len(winners) < len(vehicles):
        display_track(track, vehicles)
        for i, v in enumerate(vehicles):
            if v._position >= track_length - 1 or v in winners:
                continue
            lane = i
            pos = v._position
            obs_loc = find_next_obstacle(track, lane, pos)
            if v._initial == 'P' and v not in winners:
                print(f"\nYour turn! {v}")
                print("1. Fast\n2. Slow\n3. Special Move")
                move = check_input.get_int_range("Choose move: ", 1, 3)
                if move == 1:
                    result = v.fast(obs_loc)
                elif move == 2:
                    result = v.slow(obs_loc)
                else:
                    result = v.special_move(obs_loc)
                print(result)
            else:
                # Opponent AI
                if v._energy < 5:
                    result = v.slow(obs_loc)
                else:
                    r = rand.random()
                    if r < 0.4:
                        result = v.slow(obs_loc)
                    elif r < 0.7:
                        result = v.fast(obs_loc)
                    else:
                        result = v.special_move(obs_loc)
                print(f"{v._name}: {result}")

            # Update track
            if v._position < track_length:
                track[lane][pos] = '*'
                track[lane][v._position] = v.initial
            if v._position >= track_length - 1 and v not in winners:
                winners.append(v)
                places[i] = len(winners)

    print("\nRace Results:")
    for place, v in enumerate(winners, 1):
        print(f"{place}: {v._name}")

if __name__ == "__main__":
    main()