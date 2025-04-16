"""
This class represents the ghost and its movement.
"""
import random
from maze import Maze


class Ghost:

    def __init__(self):
        self.previous = '.'  # Represents the character beneath the ghost

    def move(self):
        """Move the ghost toward the player."""
        maze = Maze()
        gr, gc = maze.search_maze('G')
        pr, pc = maze.search_maze('P')
        maze.place_char(gr, gc, self.previous)  # Restores the previous character

        # Calculates direction toward the player
        new_gr, new_gc = gr, gc
        if gr < pr:
            new_gr += 1
        elif gr > pr:
            new_gr -= 1
        elif gc < pc:
            new_gc += 1
        elif gc > pc:
            new_gc -= 1

        # Checks if the move catches the player
        if maze[new_gr][new_gc] == 'P':
            maze.place_char(new_gr, new_gc, 'G')
            return True

        # Ensures the ghost does not move into a wall
        if maze.is_wall(new_gr, new_gc):
            directions = [(gr - 1, gc), (gr + 1, gc), (gr, gc - 1), (gr, gc + 1)]
            random.shuffle(directions)
            for new_gr, new_gc in directions:
                if not maze.is_wall(new_gr, new_gc) and maze[new_gr][new_gc] != 'P':
                    break
            else:
                new_gr, new_gc = gr, gc  # Stay in place if no valid move

        # Updates ghost's position
        self.previous = maze[new_gr][new_gc]
        maze.place_char(new_gr, new_gc, 'G')
        return False