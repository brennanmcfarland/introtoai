import cmd
import sys
import random
import time
from SearchAStar import SearchAStar
from SearchLocalBeam import SearchLocalBeam
from EightPuzzle import EightPuzzleState
from PocketCube import PocketCubeState
from enum import Enum


class Mode(Enum):
    EIGHT_PUZZLE = "eight_puzzle"
    POCKET_CUBE = "pocket_cube"


class CommandLoop(cmd.Cmd):
    """The main command loop.  Note that methods are required to be in the format do_<command syntax> to work.
    do_commandName executes whenever commandName is typed in, with any arguments automatically parsed from the
    input string."""

    mode = Mode.EIGHT_PUZZLE
    puzzle_state = None
    max_nodes = 0

    def __init__(self, stdin=sys.stdin):
        random.seed(4096) # as specified in the assignment, the seed is set to a static value
        self.do_setMode("8-puzzle")
        self.use_rawinput = False
        super().__init__(stdin=stdin, stdout=None)

    def do_help(self, arg):
        self.print_help()

    def do_setMode(self, mode_string):
        if mode_string == "8-puzzle":
            self.mode = Mode.EIGHT_PUZZLE
            self.puzzle_state = self.set_eight_puzzle_state("b12 345 678")
        elif mode_string == "pocket-cube":
            self.mode = Mode.POCKET_CUBE
            self.puzzle_state = self.set_pocket_cube_state("wwww yyoo rrgg yyoo rrgg bbbb")

    def do_setState(self, state_string):
        """Set the state"""
        if self.mode == Mode.EIGHT_PUZZLE:
            self.puzzle_state = self.set_eight_puzzle_state(state_string)
        else:
            self.puzzle_state = self.set_pocket_cube_state(state_string)
        print("State set to " + state_string)

    def do_randomizeState(self, move_count_string):
        """Randomize the state in such a way as it is still solvable"""
        try:
            move_count = int(move_count_string)
        except ValueError:
            self.print_help()
            return
        for move_index in range(0, move_count):
            current_neighbors = self.puzzle_state.neighbors
            random_neighbor_index = random.randint(0, len(current_neighbors)-1)
            # resets the state's parent & last move
            if self.mode == Mode.EIGHT_PUZZLE:
                self.puzzle_state = current_neighbors[random_neighbor_index]
                self.puzzle_state = EightPuzzleState(self.puzzle_state.get_tiles()) # resets the state's aux data
            else:
                self.puzzle_state = current_neighbors[random_neighbor_index]
                self.puzzle_state = PocketCubeState(self.puzzle_state.get_tiles())
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
        start_time = time.time()
        algorithm_args = algorithm_string.split()
        result = None
        if len(algorithm_args) != 2: # argument 1: algorithm, argument 2: heuristic/k
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
        if result == "already in goal state":
            print(result)
        elif result:
            print(len(result), "moves: ", result, " in ", time.time()-start_time, " seconds")
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
        """When read from a file, the cmd must be told how to deal with an EOF"""
        return True

    def set_eight_puzzle_state(self, state_string):
        """Takes a string in the format b12 345 678 and returns the corresponding eight puzzle state"""
        state_list = []
        for state_string_char in state_string.replace(" ", ""):
            if state_string_char == 'b':
                state_list.append(0)
            else:
                state_list.append(int(state_string_char))
        return EightPuzzleState(tuple(state_list))

    def set_pocket_cube_state(self, state_string):
        state_list = []
        for state_string_char in state_string.replace(" ", ""):
            state_list.append(state_string_char)
        state_tuple = PocketCubeState(tuple(state_list))
        return state_tuple

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
