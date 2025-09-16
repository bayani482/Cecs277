"""LAB 4
09/15/2025

Student 1: Javier Jacobo
Student 2: Bryan Bayani

This is a program that reads in a file and creates a maze, in which the user must select 1-4 translating to up,down,right,left.
each input is validated for a integer value. If you try to go in a direction where there is a *, you will prompted that you cannot 
go there and pick another direction. You win the game once you get the X to the f

"""

import check_input


def read_maze():
    """function this function create 2d list from reading a file and adding each character as a seperate element
        OUTPUT: returns list
    """
    maze_2d = []
    with open("maze.txt", "r") as maze:
        for line in maze:
            row = list(line.strip("\n"))
            maze_2d.append(row)
    return maze_2d


def find_start(maze):
    """function this function takes in the list and searches the list for the s and returns the index as two seperate integers
        OUTPUT: returns two integers
        INPUT:  list -  maze which each character as a seperate element
    """
    for r, row in enumerate(maze):
        for c, value in enumerate(row):
            if value == "s":
                startRowIndex = r
                startColIndex = c
    return startRowIndex, startColIndex


def display_maze(maze, loc):
    """function this function takes in 2 lists and prints out the game state of users location
        INPUT:  list - maze which each character as a seperate element
                list - two integers as the (row,col) of the users current location
    """
    for r, row in enumerate(maze):
        for c, value in enumerate(row):
            if (r, c) == loc:
                print("X", end=" ")
            else:
                print(value, end=" ")
        print()


def main():
    print("-Maze Solver-")
    maze = read_maze()
    row, col = find_start(maze)
    userLoc = [row, col]
    play = True
    while play:
        display_maze(maze, userLoc)
        userInput = int(check_input.get_int_range("1. Go North\n2. Go South\n3. Go East\n4. Go West\nEnter Choice:", 1, 4))
        moveRow, moveCol = row, col
        match userInput:
            case 1:  # north
                moveRow -= 1
            case 2:  # south
                moveRow += 1
            case 3:  # east
                moveCol += 1
            case 4:  # west
                moveCol -= 1

        if moveRow < 0 or moveRow >= len(maze) or moveCol < 0 or moveCol >= len(maze[row]):
            print("You cannot move there")
            continue

        if maze[moveRow][moveCol] == "*":
            print("You cannot move there")
            continue

        row, col = moveRow, moveCol
        #print(userLoc)
        userLoc = (row, col)
        row, col = moveRow, moveCol

        if maze[row][col] == "f":
            display_maze(maze, userLoc)
            print("Congratulations! You solved the maze.")
            play = False


if __name__ == "__main__":
    main()
