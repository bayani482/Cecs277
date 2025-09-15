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
            items = row.strip().split(" ")
            maze_2d.append(items)

    for row in maze_2d:
        print (" ".join(map(str,row)))

    return maze_2d

def find_start(maze):
    for row in maze:
        for column in row:
            if 's' == column:
                index_of_s = maze.index(column)
                print(index_of_s)

#def display_maze(maze, loc):

def main():

    maze = read_maze()
    find_start(maze)
    
if __name__ == '__main__':
    main()