from SearchAStar import SearchAStar
from EightPuzzle import EightPuzzleState

a_star = SearchAStar()
test_puzzle_state = EightPuzzleState((1, 2, 5, 3, 8, 4, 6, 0, 7))
print(test_puzzle_state)
result = a_star.search(test_puzzle_state, True)
print(result)
