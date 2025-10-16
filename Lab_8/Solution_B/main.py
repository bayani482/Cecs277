
import random as rand

import car
import check_input
import motorcycle
import truck


def create_track(vehicles):
    track = []
    for v in vehicles:
        lane = ['-' for _ in range(100)]
        for _ in range(2):
            obstacle_pos = rand.randint(10, 99)
            lane[obstacle_pos] = '0'
        lane[0] = v.initial
        track.append(lane)
    return track

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

    
    # Prompt user to choose a vehicle
    print("Red Racer!\nChoose a vehicle and race it down the track (player = 'P'). Slow down for obstacles ('0') or else you'll crash!")
    print("1. Lightning Car - a fast car. Speed: 7. Special: Nitro Boost (1.5x speed)\n2. Swift Bike - a speedy motorcycle. Speed: 8. Special: Wheelie (2x speed but there's a chance you'll wipe out).\n3. Behemoth Truck - a heavy truck. Speed: 6. Special: Ram (2x speed and it smashes through obstacles).")
    

    
    choice = check_input.get_int_range("Choose your Vehicle(1-3): ", 1, 3) -1
    # Create vehicle objects
    vehicles = []
    for i in range(3):
        if vehicles_names[i] == 'Lightning Car':
            vehicles.append(car.Car(vehicles_names[i], vehicle_letters[i], vehicle_speeds[i]))
        elif vehicles_names[i] == 'Swift Bike':
            vehicles.append(motorcycle.Motorcycle(vehicles_names[i], vehicle_letters[i], vehicle_speeds[i]))
        elif vehicles_names[i] == 'Behemoth Truck':
            vehicles.append(truck.Truck(vehicles_names[i], vehicle_letters[i], vehicle_speeds[i]))

    vehicles[choice]._initial = 'P'
    player_vehicle = choice
    track = create_track(vehicles)
    winners = []
    places = [None, None, None]
    while len(winners) < len(vehicles):
        display_track(track, vehicles)

        # -------- Player turn first --------
        i = player_vehicle
        v = vehicles[i]
        if v not in winners and v.position < track_length - 1:
            lane = i
            pos = v.position
            obs_loc = find_next_obstacle(track, lane, pos)  # distance or None

            move = check_input.get_int_range(
                "Choose your action: (1. Fast, 2. Slow, 3. Special Move): ", 1, 3
            )
            if move == 1:
                result = v.fast(obs_loc)
            elif move == 2:
                result = v.slow(obs_loc)
            else:
                result = v.special_move(obs_loc)
            print(result)

            # Update track for player
            if v.position < track_length:
                track[lane][pos] = '*'
                track[lane][v.position] = v.initial
            if v.position >= track_length - 1 and v not in winners:
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
    # while len(winners) < len(vehicles):
    #     display_track(track, vehicles)
        
    #     for i, v in enumerate(vehicles):
    #         if v.position >= track_length - 1 or v in winners:
    #             continue
    #         lane = i
    #         pos = v.position
    #         obs_loc = find_next_obstacle(track, lane, pos)
    #         if v.initial == 'P' and v not in winners:
    #             move = check_input.get_int_range("Choose your action: (1. Fast, 2. Slow, 3. Special Move): ", 1, 3)
    #             if move == 1:
    #                 result = v.fast(obs_loc)
    #             elif move == 2:
    #                 result = v.slow(obs_loc)
    #             else:
    #                 result = v.special_move(obs_loc)
    #             print(result)
    #         else:
    #             # Opponent AI
    #             if v.energy < 5:
    #                 result = v.slow(obs_loc)
    #             else:
    #                 r = rand.random()
    #                 if r < 0.4:
    #                     result = v.slow(obs_loc)
    #                 elif r < 0.7:
    #                     result = v.fast(obs_loc)
    #                 else:
    #                     result = v.special_move(obs_loc)
    #             print(f"{v._name}: {result}")
            
    #         # Update track
    #         if v.position < track_length:
    #             track[lane][pos] = '*'
    #             track[lane][v.position] = v.initial
    #         if v.position >= track_length - 1 and v not in winners:
    #             winners.append(v)
    #             places[i] = len(winners)
    #     print()
    
    print("\nRace Results:")
    for place, v in enumerate(winners, 1):
        print(f"{place}: {v.name}")

if __name__ == "__main__":
    main()