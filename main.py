"""
Aldo Fernandez and Dylan Dougherty
Date: April 8, 2025
Description: Pacman game where the player is in a maze and has to eat all the dots while avoiding a ghost.
"""

from maze import Maze
from player import Player
from ghost import Ghost

def main():
    """Runs the Pacman game """
    maze = Maze()
    player = Player()
    ghost = Ghost()

    while True:
        print(maze)
        move = input("Move (WASD): ").lower()

        if move not in ['w', 'a', 's', 'd']:
            print("Invalid input. Try again.")
            continue

        # Moves the player
        if player.move(move):
            print(maze)
            print("You ran into the ghost! Game over...")
            break

        # Moves the ghost
        if ghost.move():
            print(maze)
            print("The ghost caught you! Game over...")
            break

        # Checks if all dots are eaten by pacman
        if maze.count_dots() == 0:
            print(maze)
            print("All dots eaten. You win!")
            break

if __name__ == "__main__":
    main()