from car import Car
import check_input

car1 = Car("Cool car",0,10)
obs_loc = 40

play = True

while play:

    print(car1)

    move_choice = check_input.get_int_range("1. Fast\n2. Slow\n3. Special Move\n>>",1,3)

    match move_choice:
        case 1:
            car1.fast(obs_loc)
        case 2:
            car1.slow(obs_loc)
        case 3:
            car1.special_move(obs_loc)
        


