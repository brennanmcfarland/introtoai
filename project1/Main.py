import cmd
import sys
import random
from SearchAStar import SearchAStar
from SearchLocalBeam import SearchLocalBeam
from EightPuzzle import EightPuzzleState
from enum import Enum


class Mode(Enum):
    EIGHT_PUZZLE = "eight_puzzle"
    POCKET_CUBE = "pocket_cube"


class CommandLoop(cmd.Cmd):
    """The main command loop.  Note that methods are required to be in the format do_<command syntax> to work."""

    # TODO: commands should always operate on the current puzzle state, so make sure there's always one and only one such state

    mode = Mode.EIGHT_PUZZLE
    puzzle_state = None
    max_nodes = 0

    def __init__(self, stdin=sys.stdin):
        random.seed(4096) # as specified in the assignment, the seed is set to a static value
        self.puzzle_state = self.set_eight_puzzle_state("b12 345 678")
        self.use_rawinput = False
        super().__init__(stdin=stdin, stdout=None)

    def do_help(self, arg):
        self.print_help()

    def do_setState(self, state_string):
        """Set the state"""
        self.puzzle_state = self.set_eight_puzzle_state(state_string)
        print("State set to " + state_string)

    def do_randomizeState(self, move_count_string):
        """Randomize the state in such a way as it is still solvable"""
        try:
            move_count = int(move_count_string)
        except ValueError:
            self.print_help() # TODO: can I convert these to just return self.print_help()?
            return
        for move_index in range(0, move_count):
            current_neighbors = self.puzzle_state.neighbors
            random_neighbor_index = random.randint(0, len(current_neighbors)-1)
            self.puzzle_state = current_neighbors[random_neighbor_index]
            self.puzzle_state = EightPuzzleState(self.puzzle_state.get_tiles())
        self.print_state()

    def do_printState(self, arg):
        """Print the current state of the puzzle"""
        self.print_state()

    def do_move(self, direction):
        """Make a move in the specified direction"""
        if self.mode != Mode.EIGHT_PUZZLE:
            print("Cannot make move outside of eight-puzzle mode")
            return
        elif direction == "left":
            self.puzzle_state = self.puzzle_state.left
        elif direction == "right":
            self.puzzle_state = self.puzzle_state.right
        elif direction == "up":
            self.puzzle_state = self.puzzle_state.up
        elif direction == "down":
            self.puzzle_state = self.puzzle_state.down
        else:
            print("Invalid move")
            return
        self.print_state()

    def do_solve(self, algorithm_string):
        """Solve the current state with the given algorithm (and heuristic if it is required to specify)"""
        algorithm_args = algorithm_string.split()
        result = None
        if len(algorithm_args) != 2:
            self.print_help()
            return
        elif algorithm_args[0] == "A-star":
            result = self.solve_A_star(algorithm_args[1])
        elif algorithm_args[0] == "beam":
            try:
                result = SearchLocalBeam().search(self.puzzle_state, int(algorithm_args[1]), self.max_nodes)
            except ValueError:
                self.print_help()
        else:
            self.print_help()
        if result:
            print(len(result), "moves: ", result)
        else:
            print("Max search nodes exceeded")
        self.puzzle_state = EightPuzzleState(self.puzzle_state.get_tiles())

    def do_maxNodes(self, max_nodes):
        try:
            self.max_nodes = int(max_nodes)
        except ValueError:
            self.print_help()
    def do_stop(self, arg):
        return True

    def do_close(self, arg):
        return True

    def do_exit(self, arg):
        return True

    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
        return True

    # TODO: error checking?
    def set_eight_puzzle_state(self, state_string):
        """Takes a string in the format b12 345 678 and returns the corresponding eight puzzle state"""
        state_list = []
        for state_string_char in state_string.replace(" ", ""):
            if state_string_char == 'b':
                state_list.append(0)
            else:
                state_list.append(int(state_string_char))
        state_tuple = tuple(state_list)
        if self.mode == Mode.EIGHT_PUZZLE:
            return EightPuzzleState(state_tuple)
        else:
            pass  # TODO: return new pocket cube state

    def solve_A_star(self, heuristic_string):
        """Solves the current puzzle state with A* using either h1 or h2 depending on input"""
        if heuristic_string == "h1":
            return SearchAStar().search(self.puzzle_state, False, self.max_nodes)
        elif heuristic_string == "h2":
            return SearchAStar().search(self.puzzle_state, True, self.max_nodes)
        else:
            self.print_help()
            return None

    def print_state(self):
        print(self.puzzle_state)

    def print_help(self):
        print("Valid commands: \n"
              + "setState <state>: Set the puzzle's current state, in the format b12 345 678 for the 8-puzzle.")


def process_input_arguments():
    if len(sys.argv) > 2:
        print(sys.argv)
        print("Error: too many arguments.  Specify either a filename to read commands from or no arguments for a"
              + " command line.")
        exit()
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        return CommandLoop(stdin=open(filename))
    return CommandLoop()


command_loop = process_input_arguments()
command_loop.cmdloop()

# a_star = SearchAStar()
# initial_state = EightPuzzleState((1, 2, 5, 3, 4, 8, 6, 0, 7))
# print(initial_state)
# result = a_star.search(initial_state, True)
# print(result)
