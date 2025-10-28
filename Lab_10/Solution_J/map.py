class Map:
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Map, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not Map._initialized:
            # Load the map from map.txt
            try:
                with open('map.txt', 'r') as file:
                    self._map = []
                    for line in file:
                        self._map.append(list(line.strip()))
            except FileNotFoundError:
                print("Error: map.txt file not found")
                self._map = []
            
            Map._initialized = True

    def __getitem__(self, row):
        return self._map[row]

    def __len__(self):
        return len(self._map)
    
    def show_map(self,loc):
        x, y = loc
        for i, row in enumerate(self._map):
            for j, col in enumerate(row):
                if (i, j) == (x, y):
                    print(f"[{col}]", end="")
                else:
                    print(f" {col} ", end="")
            print()

    def reveal(self, loc):
        x, y = loc
        if 0 <= x < len(self._map) and 0 <= y < len(self._map[0]):
            return self._map[x][y]
        else:
            return 'o'
        
    def remove_at_loc(self, loc):
        x, y = loc
        if 0 <= x < len(self._map) and 0 <= y < len(self._map[0]):
            self._map[x][y] = 'n'