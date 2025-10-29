"""_summary_


"""


class Map:
    _instance = None
    _initialized = False
    
    def __new__(cls):
        """_summary_

        Returns:
            _type_: _description_
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    def __init__(self):
        """_summary_
        """
        if Map._initialized:
            return
        ## read file and make map
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
            row (_type_): _description_

        Returns:
            _type_: _description_
        """
        return self._map[row]
    
    def __len__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return len(self._map)
    
    def show_map(self,loc):
        """_summary_

        Args:
            loc (_type_): _description_

        Returns:
            _type_: _description_
        """
        rH, cH = loc
        output = ""
        for row in range(len(self._map)):
            for col in range(len(self._map[row])):
                if row == rH and col == cH:
                    output += "*"# hero postion
                elif self._revealed[row][col]:
                    output += self._map[row][col]  # revealed tile
                else:
                    output += "x"  # unrevealed tile
            output += "\n"  # next row
        return output
    
    def reveal(self,loc):
        """_summary_

        Args:
            loc (_type_): _description_

        Returns:
            _type_: _description_
        """
        row, col = loc
        self._revealed[row][col] = True
        return self._map[row][col]
    def remove_at_loc(self,loc):
        """_summary_

        Args:
            loc (_type_): _description_
        """
        row, col = loc
        self._map[row][col] = "n"
