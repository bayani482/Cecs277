""" LAB 4
    09/15/2025

    Student 1: Javier Jacobo
    Student 2: Bryan Bayani

"""

import check_input


def read_maze():
    maze_2d = []
    with open("maze.txt", "r") as maze:
        for row in maze:
            items = row.strip()
            maze_2d.append(items)
    return maze_2d

def find_start(maze):
    for row_index, row in enumerate(maze):
        for col_index, value in enumerate(row):
            if value == "s":
                startRowIndex = row_index
                startColIndex = col_index
    return startRowIndex, startColIndex


def display_maze(maze, loc):
    print(loc)
    for row in maze:
        for element in row:
            print(element, end=' ')
        print()
    
def main():
    maze = read_maze()
    display_maze(maze,find_start(maze))
    
if __name__ == '__main__':
    main()