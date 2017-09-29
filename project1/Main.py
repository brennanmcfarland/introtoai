import cmd
import sys
from SearchAStar import SearchAStar
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

    def __init__(self, stdin=sys.stdin):
        self.use_rawinput = False
        sys.stdout = old_stdout
        super().__init__(stdin=stdin, stdout=sys.stdout)

    def do_help(self, arg):
        print("Valid commands: \n"
              + "setState <state>: Set the puzzle's current state, in the format b12 345 678 for the 8-puzzle.")

    def do_setState(self, state_string):
        """Set the state"""
        self.puzzle_state = self.set_eight_puzzle_state(state_string)
        print("State set to " + state_string)

    def do_stop(self, arg):
        return True

    def do_close(self, arg):
        return True

    def do_exit(self, arg):
        return True

    def do_quit(self, arg):
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


old_stdout = sys.__stdout__
try:
    command_loop = process_input_arguments()
    command_loop.cmdloop()
except:
    pass

# a_star = SearchAStar()
# initial_state = EightPuzzleState((1, 2, 5, 3, 8, 4, 6, 0, 7))
# print(initial_state)
# result = a_star.search(initial_state, True)
# print(result)
