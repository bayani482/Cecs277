"""
Lab 12 - Decorators

Student 1: Bryan Bayani
Student 2: Javier Jacobo
Date: November 10th, 2025

A fun, whimsical, and awesome Thanksgiving Simulator.
Stuff your mouth with all the classics:
Turkey, Stuffing, Potatoes, Green_Beans, and Pie.... Yummy
"""
import check_input
from small_plate import SmallPlate
from large_plate import LargePlate
from turkey import Turkey
from stuffing import Stuffing
from potatoes import Potatoes
from green_beans import GreenBeans
from pie import Pie



def examine_plate(plate):
    """
    Examines the plate to see if it can hold the food
    
    Args:
        plate (PlateDecorator): The current plate with food items
    Returns:
        result: bool -- True if the plate can hold the food, False otherwise
    """
    result = False
    print(plate.description())

    # Check weight
    if plate.weight() >= 13:
        weight_hint = "Sturdiness: Strong"
        result = True
    elif plate.weight() >= 7:
        weight_hint = "Sturdiness: Weak"
        result = True
    elif plate.weight() >= 1:
        weight_hint = "Sturdiness: Bending"
        result = True
    else:
        weight_hint = "Oh no... Your plate fell apart."
        result = False

    # Check area
    if plate.area() >= 41:
        area_hint = "Space available: Plenty"
        result = True
    elif plate.area() >= 21:
        area_hint = "Space available: Some"
        result = True
    elif plate.area() >= 1:
        area_hint = "Space available: Little"
        result = True
    else:
        area_hint = "Oh no... Your plate is full."
        result = False

    print(weight_hint)
    print(area_hint)
    return result

def main():
    play = True

    print("""
-- Thanks Giving Dinner --
Serve yourself as much food as you
like from the buffet, but make sure
that your plate will hold without
spilling everywhere!""")
    plate_choice = check_input.get_int_range("Choose a plate:\n1. Small Sturdy Plate\n2. Large Flimsy Plate\n>",1,2)

    match plate_choice:
        case 1:
            plate = SmallPlate()
        case 2:
            plate = LargePlate()
     
    # For debugging purposes, comment out below to see plate area and weight :3
    # max_weight = plate.weight()
    # max_area = plate.area()
    # print(max_weight)
    # print(max_area)

    while play:
        menu_choice = check_input.get_int_range("""1. Turkey
2. Stuffing
3. Potatoes
4. Green Beans
5. Pie
6. Quit\n>""",1,6)
        match menu_choice:
            case 1:
                plate = Turkey(plate)
            case 2:
                plate = Stuffing(plate)
            case 3:
                plate = Potatoes(plate)
            case 4:
                plate = GreenBeans(plate)
            case 5:
                plate = Pie(plate)
            case 6:
                print(f"""
Congrats! You made it to the end of the table with {plate.count()} items without spilling your food!
There was still {plate.area()} square inches of food left on your plate.
Your plate could have held {plate.weight()} more ounces of food.
Don't worry, you can always go back for more. Happy Thankgiving!""")
                break

        play = examine_plate(plate)

if __name__ == "__main__":
    main()