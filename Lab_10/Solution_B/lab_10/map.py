"""_summary_
singleton
create instance of map

"""


class Map:
    _instance = None
    _initialized = False
    
    def __new__(cls):
        """create or return instance of map

        Returns:
            Map: instance of map
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    def __init__(self):
        """
        initialize a map from file map.txt
        """
        if Map._initialized:
            return
        self._map = []
        with open("map.txt", "r") as f:
            for line in f:
                row = list(line.strip("\n"))
                if row:
                    self._map.append(row)
        self._revealed = [[False for _ in row] for row in self._map]
        Map._initialized = True

    def __getitem__(self,row):
        """get i from row in the map

        Args:
            row (int): row index

        Returns:
            list[str]: get a list of characters on the row
        """
        return self._map[row]
    
    def __len__(self):
        """return number of rows in the map

        Returns:
            int: rows in the map
        """
        return len(self._map)
    
    def show_map(self,loc):
        """go through the map and process the hero location and travled locations

        Args:
            loc (tuple[int,int]): row,col location of the hero

        Returns:
            str: string representation of the map
        """
        rH, cH = loc
        output = ""
        for row in range(len(self._map)):
            for col in range(len(self._map[row])):
                if row == rH and col == cH:
                    output += "* "
                elif self._revealed[row][col]:
                    output += self._map[row][col] + " "
                else:
                    output += "x "
            output += "\n"
        return output
    
    def reveal(self,loc):
        """reveals specific tile on the map and returns its character value

        Args:
            loc (tuple[int,int]): the (row,col) location to reveal

        Returns:
            str: character at the revealed location
        """
        row, col = loc
        self._revealed[row][col] = True
        return self._map[row][col]
    def remove_at_loc(self,loc):
        """replace the tile at a given location with 'n'

        Args:
            loc (tuple [int,int]): the (row,col) coordinates of the tile
        """
        row, col = loc
        self._map[row][col] = "n"
