from SearchAStar import SearchAStar
from EightPuzzle import EightPuzzleState

a_star = SearchAStar()
test_puzzle_state = EightPuzzleState((1, 2, 3, 4, 5, 6, 7, 8, 0))
print(test_puzzle_state)
result = a_star.search(test_puzzle_state, True)
print(result)
