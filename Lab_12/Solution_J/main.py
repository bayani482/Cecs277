"""
Lab 12 - Decorators

Student 1: Bryan Bayani
Student 2: Javier Jacobo
Date: November 10th, 2025


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
    print(plate.description())


play = True

print("""
-- Thanks Giving Dinner --
Serve yourself as much food as you
like from the buffet, but make sure
that your plate will hold without
spilling everywhere!""")
plate = 0 # temp value
plate_choice = check_input.get_int_range("Choose a plate:\n1. Small Sturdy Plate\n2. Large Flimsy Plate\n>",1,2)

match plate_choice:
    case 1:
        plate = SmallPlate()
    case 2:
        plate = LargePlate()

while play:
    examine_plate(plate)
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
            break