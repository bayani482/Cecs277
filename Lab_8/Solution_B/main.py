"""
LAB 8

Student 1: Javier Jacobo
Student 2: Bryan Bayani

A program that generates a new track and allows the user to race against two computer opponents.

"""
import random as rand

import check_input
from car import Car
from motorcycle import Motorcycle
from truck import Truck


def display_track(track, vehicles):
    #print vehicle status
    for i in vehicles:
        print(i)
    #print track
    for i in track:
        print(''.join(i))

def find_next_obstacle(track, lane, pos):
    row = track[lane]
    for i in range(pos + 1, len(row)):
        if row[i] == '0':
            return i - pos
    return None

def main():
    vehicles_names = ['Lightning Car','Swift Bike','Behemoth Truck']
    vehicle_letters = ['C','M','T']
    vehicle_speeds = [7,8,6]
    track_length = 100
    winners = []
    vehicles = []
    places = [None, None, None]
    print("Red Racer!\nChoose a vehicle and race it down the track (player = 'P'). Slow down for obstacles ('0') or else you'll crash!")
    print("1. Lightning Car - a fast car. Speed: 7. Special: Nitro Boost (1.5x speed)")
    print("2. Swift Bike - a speedy motorcycle. Speed: 8. Special: Wheelie (2x speed but there's a chance you'll wipe out).")
    print("3. Behemoth Truck - a heavy truck. Speed: 6. Special: Ram (2x speed and it smashes through obstacles).")
    choice = check_input.get_int_range("Enter choice(1-3): ", 1, 3) - 1

    for i in range(3):
        if vehicles_names[i] == 'Car':
            vehicles.append(Car(vehicles_names[i], vehicle_letters[i], vehicle_speeds[i]))
        elif vehicles_names[i] == 'Motorcycle':
            vehicles.append(Motorcycle(vehicles_names[i], vehicle_letters[i], vehicle_speeds[i]))
        else:
            vehicles.append(Truck(vehicles_names[i], vehicle_letters[i], vehicle_speeds[i]))  # Placeholder for Truck
            
    vehicles[choice]._initial = 'P'
    player_vehicle = choice


    track = []# create track
    for v in vehicles:
        lane = ['-' for _ in range(track_length)]
        for _ in range(2):
            obstacle_pos = rand.randint(10, track_length - 1)
            lane[obstacle_pos] = '0'
        lane[0] = v.initial
        track.append(lane)


    
    while len(winners) < len(vehicles):
        display_track(track, vehicles)
        for i, v in enumerate(vehicles):
            if v.position >= track_length - 1 or v in winners:
                continue
            lane = i
            pos = v.position
            obs_loc = find_next_obstacle(track, lane, pos)
            if v.initial == 'P' and v not in winners:
                move = check_input.get_int_range("Choose your action: (1. Fast, 2. Slow, 3. Special Move): ", 1, 3)
                if move == 1:
                    result = v.fast(obs_loc)
                elif move == 2:
                    result = v.slow(obs_loc)
                else:
                    result = v.special_move(obs_loc)
                print(f"{v._name}: {result}")
            else:
                # Opponent AI
                if v.energy < 5:
                    result = v.slow(obs_loc)
                else:
                    r = rand.random()
                    if r < 0.4:
                        result = v.slow(obs_loc)
                    elif r < 0.7:
                        result = v.fast(obs_loc)
                    else:
                        result = v.special_move(obs_loc)
                #print(f"{v._name}: {result}")

            # Update track
            if v.position < track_length:
                track[lane][pos] = '*'
                track[lane][v._position] = v.initial
            if v._position >= track_length - 1 and v not in winners:
                winners.append(v)
                places[i] = len(winners)

        # -------- Opponents --------
        for j, u in enumerate(vehicles):
            if j == player_vehicle:
                continue
            if u in winners or u.position >= track_length - 1:
                continue

            lane = j
            pos = u.position
            obs_loc = find_next_obstacle(track, lane, pos)  # distance or None

            # Simple AI
            if u.energy < 5:
                result = u.slow(obs_loc)
            else:
                r = rand.random()
                if r < 0.4:
                    result = u.slow(obs_loc)
                elif r < 0.7:
                    result = u.fast(obs_loc)
                else:
                    result = u.special_move(obs_loc)
            print(f"{u._name}: {result}")

            # Update track for AI
            if u.position < track_length:
                track[lane][pos] = '*'
                track[lane][u.position] = u.initial
            if u.position >= track_length - 1 and u not in winners:
                winners.append(u)
                places[j] = len(winners)
        print()
    print("\nRace Results:")
    for place, v in enumerate(winners, 1):
        print(f"{place}: {v.name}")

if __name__ == "__main__":
    main()