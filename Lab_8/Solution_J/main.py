import random as rand
from car import Car
from motorcycle import Motorcycle
from vehicle import Vehicle
from truck import Truck
import check_input


def display_track(track):
    for lane in track:
            print("".join(lane))

def current_pos_and_initial(vehicles,lane_index):    # function to get current position and initial of vehicle in given lane
    v = vehicles[lane_index]
    return v.get_position(), v.get_initial()

def main():
    """Run the race without accessing private attributes from main.
    - Track: 3 lanes x 100 units (only 'track' 2D list used).
    - 'vehicles' list contains the three vehicle objects (no extra lists).
    """
    lanes = 3
    track_length = 100
    
    track = []
    for _ in range(lanes): # Create empty track (3x100) with '-' in each lane
        lane = list("-" * track_length)
        track.append(lane)

    # Vehicles list
    vehicles = [Car("Lightning Car", "C", 7), Motorcycle("Swift Bike", "M", 6), Truck("Behemoth Truck", "T", 8)]

    if track_length > 2: # Place 2 obstacles ('0') in each lane at random positions

        for lane in range(lanes):
            p1 = rand.randrange(1, track_length - 1)  # Get two random positions for obstacles
            p2 = rand.randrange(1, track_length - 1)
            while p2 == p1:  # Check that obstacles are not in the same position
                p2 = rand.randrange(1, track_length - 1)
            track[lane][p1] = "0"
            track[lane][p2] = "0"

    print("Rad Racer!")
    print("Choose a Vehicle and race it down the track (player = 'P'). Slow down for obstacles ('0') or else you'll crash!")
    print("""
 1. Lightning Car - a fast car. Speed: 7. Special: Nitro Boost (1.5x speed)
 2. Swift Bike - a speedy motorcycle. Speed: 6. Special Wheelie (2x speed but there's a chance you'll wipe out)
 3. Behemoth Truck - a heavy truck. Speed: 8. Special: Ram (2x speed and it smashes through obstacles).
 """)
    choice = check_input.get_int_range("Choose your vehicle (1-3): ", 1, 3)
    player_index = choice - 1
    vehicles[player_index].set_initial("P")
    
    for lane in range(lanes): # Place vehicle initials at starting positions
        v = vehicles[lane]
        track[lane][0] = v.get_initial()[0]

    places = [] # List to record first, second, third places

    while len(places) < 3: # Main while loop. Will run until all vehicles finish
        print()

        for vehicle in vehicles:
            print(vehicle)

        display_track(track)

        player_finished = vehicles[player_index].get_position() >= track_length - 1 # Check if player has finished

        if not player_finished: # If player hasn't finished, get their action choice
            action_choice = check_input.get_int_range("Choose action (1. Fast, 2. Slow, 3. Special Move): ", 1, 3)
            match action_choice:
                case 1:
                    player_action = "fast"
                case 2:
                    player_action = "slow"
                case 3:
                    player_action = "special"
        else:
            player_action = None

        lane = 0
        while lane < lanes:
            v = vehicles[lane]
            pos = v.get_position()
            init = v.get_initial()

            if pos >= track_length - 1: # If vehicle already finished, skip its turn
                if v not in places:
                    places.append(v)
                lane += 1
                continue

            # find next obstacle index after current position (public track usage)
            row = track[lane]
            if "0" in row[pos+1:]:
                next_obs = row.index("0", pos + 1)
            else:
                next_obs = track_length

            # decide action for this vehicle
            if lane == player_index and not player_finished:
                action = player_action
            else:
                energy_val = v.get_energy()
                if energy_val is not None and energy_val <= 0:
                    action = "slow"
                else:
                    r = rand.random()
                    if r < 0.40:
                        action = "slow"
                    elif r < 0.70:
                        action = "fast"
                    else:
                        action = "special"

            # call movement method with next obstacle location and print its description
            old_pos = v.get_position()
            if action == "fast":
                print(v.fast(next_obs))
            elif action == "slow":
                print(v.slow(next_obs))
            else:
                print(v.special_move(next_obs))
            

            # cap positions before using them to index the track to avoid IndexError
            new_pos = v.get_position()
 
            last_index = track_length - 1
            old_pos_capped = min(max(old_pos, 0), last_index)
            new_pos_capped = min(max(new_pos, 0), last_index)

            if track[lane][old_pos_capped] != "0":  # Change old position with '*'. Leave obstacle as '0' if present
                track[lane][old_pos_capped] = "*"
            # place the vehicle initial at the (capped) new position
            track[lane][new_pos_capped] = init[0]

            if new_pos >= track_length - 1:
                if v not in places:
                    places.append(v)

            lane += 1

    display_track(track)

    print("\nRace complete! Results:")
    for i, vehicle in enumerate(places, 1):
        print(f"{i}.", vehicle)

if __name__ == "__main__":
     main()