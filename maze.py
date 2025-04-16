"""
 This class implements Singleton and manages the maze grid.
 """
class Maze:

    _instance = None  # Class variable to hold the singleton instance
    _initialized = False  # Tracks if the maze has been initialized

    def __new__(cls):
        """Makes sure only one instance of Maze is created."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """Initializes the maze if it hasn't been already."""
        if not self._initialized:
            self.grid = []
            with open("pacman.txt", "r") as file:
                self.grid = [list(line.strip()) for line in file.readlines()]
            self._initialized = True

    def __getitem__(self, row):
        """ Accesses rows or specific grid elements."""
        return self.grid[row]

    def is_wall(self, r, c):
        """Checks if the location is a wall."""
        if r < 0 or r >= len(self.grid) or c < 0 or c >= len(self.grid[0]):
            return True
        return self.grid[r][c] == '*'

    def place_char(self, r, c, char):
        """Places a character at the specified location in the maze."""
        self.grid[r][c] = char

    def __str__(self):
        """Returns the maze as a string in grid format."""
        return "\n".join("".join(row) for row in self.grid)

    def search_maze(self, char):
        """Finds the first occurrence of a character in the maze."""
        for r, row in enumerate(self.grid):
            for c, cell in enumerate(row):
                if cell == char:
                    return [r, c]
        return [-1, -1]

    def count_dots(self):
        """Counts the number of dots in the maze."""
        return sum(row.count('.') for row in self.grid)