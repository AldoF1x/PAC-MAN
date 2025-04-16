"""
This class represents the player and its movement.
"""


from maze import Maze

class Player:
    def move(self, direction):
        """Moves the player in the specified direction (w,a,s,d)."""

        maze = Maze()
        row, col = maze.search_maze('P')
        maze.place_char(row, col, ' ')  # Clears the current position

        # New position
        new_row, new_col = row, col
        if direction == 'w':
            new_row -= 1
        elif direction == 'a':
            new_col -= 1
        elif direction == 's':
            new_row += 1
        elif direction == 'd':
            new_col += 1

        # Checks if the new position is valid
        if maze.is_wall(new_row, new_col):
            maze.place_char(row, col, 'P')  # Restores player to original position
            return False

        if maze[new_row][new_col] == 'G':
            maze.place_char(new_row, new_col, 'P')
            return True  # Player ran into the ghost

        maze.place_char(new_row, new_col, 'P')  # Moves the player
        return False