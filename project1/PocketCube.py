import copy

import SearchAlgorithm as Search

r, rprime, d, dprime = "r", "rprime", "d", "dprime"


class PocketCubeState(Search.NodeStateData):
    __faces = None  # a 23 element tuple of 'w','y','o','r','g','b'
    __last_move = None
    __parent = None
    # cache these values so they needn't be repeatedly calculated
    __num_faces = 0
    __num_sides = 0
    __faces_per_side = 0
    __gcost = 0

    def __new__(cls, state, gcost=0, last_move=None, parent=None):
        assert isinstance(state, tuple)
        new_cube = Search.NodeStateData.__new__(cls)
        # new_cube.__faces = copy.copy(state)
        # new_cube.__faces = state
        new_cube.__faces = tuple.__new__(tuple, state)
        new_cube.__num_faces = len(state)
        new_cube.__num_sides = 6
        new_cube.__faces_per_side = int(new_cube.__num_faces / new_cube.__num_sides)
        new_cube.__gcost = gcost
        new_cube.__last_move = last_move
        new_cube.__parent = parent
        return new_cube

    @property
    def last_move(self):
        return self.__last_move

    @property
    def goal_test(self):
        for sideIndex in range(0, self.__num_sides):
            face_color = self.__num_sides[sideIndex*self.__faces_per_side]
            for faceIndex in range(1, self.__faces_per_side):
                if not self.__faces[sideIndex*self.__faces_per_side + faceIndex].equals(face_color):
                    return False
        return True

    @property
    def gcost(self):
        return self.__gcost

    @property
    def parent(self):
        return self.__parent

    @property
    def h1cost(self):
        """Number of out-of-place faces"""
        faces = self.__faces
        hcost = 0
        for sideIndex in range(0, self.__num_sides):
            face_colors = set()
            face_colors.add(self.__num_sides[sideIndex*self.__faces_per_side])
            for faceIndex in range(1, self.__faces_per_side):
                if not face_colors.__contains__(faces[sideIndex*self.__faces_per_side + faceIndex]):
                    face_colors.add(faces[sideIndex*self.__faces_per_side + faceIndex])
                    hcost += 1
        return hcost

    @property
    def h2cost(self):
        """Sum of faces' distances from their goal state"""
        pass

    @property
    def neighbors(self):
        """Gets all states immediately reachable rom this state that was not the last state (hence __last_move)"""
        state_neighbors = []
        # add move r
        r_result = self.r
        if r_result is not self and self.__last_move != r:
            state_neighbors.append(r_result)
        # add move r prime
        rprime_result = self.rprime
        if rprime_result is not self and self.__last_move != rprime:
            state_neighbors.append(rprime_result)
        # add move d
        d_result = self.d
        if d_result is not self and self.__last_move != d:
            state_neighbors.append(d_result)
        # add move d prime
        dprime_result = self.dprime
        if dprime_result is not self and self.__last_move != dprime:
            state_neighbors.append(dprime_result)
        return tuple(state_neighbors)

    @property
    def r(self):
        new_faces = self.__faces
        for i in range(4, 11):
            new_faces = switch_in_tuple(new_faces, i, i+1)
        return PocketCubeState(new_faces, self.gcost+1, r, self)

    @property
    def rprime(self):
        new_faces = self.__faces
        for i in range(12, 5, -1):
            new_faces = switch_in_tuple(new_faces, i, i-1)
        return PocketCubeState(new_faces, self.gcost+1, rprime, self)

    @property
    def d(self):
        new_faces = self.__faces
        first_to_switch = (7, 15, 14, 8, 16, 21, 20, 13, 5, 2)
        second_to_switch = (15, 14, 6, 16, 21, 20, 13, 5, 2, 3)
        for i in range(len(first_to_switch)):
            new_faces = switch_in_tuple(new_faces, first_to_switch[i], second_to_switch[i])
        return PocketCubeState(new_faces, self.gcost+1, d, self)

    @property
    def dprime(self):
        new_faces = self.__faces
        first_to_switch = (2, 5, 13, 20, 21, 16, 8, 14, 15, 7)
        second_to_switch = (3, 2, 5, 13, 20, 21, 16, 6, 14, 15)
        for i in range(len(first_to_switch)):
            new_faces = switch_in_tuple(new_faces, first_to_switch[i], second_to_switch[i])
        return PocketCubeState(new_faces, self.gcost+1, dprime, self)

    def get_tiles(self):
        return copy.copy(self.__faces)

    def __eq__(self, other):
        if isinstance(self, other):
            return self.__faces == other.__faces
        else:
            return False

    def __lt__(self, other):
        return self.__faces < other.__faces

    def __hash__(self):
        hash_value = 0
        for i in range(0, self.__num_faces):
            hash_value += (i + 1) * self.__num_faces * self.__faces[i]
        return hash_value

    def __str__(self):
        return str(self.__faces)


def switch_in_tuple(tuple_to_permute, i, j):
    """return the given tuple with the elements at indices i and j switched"""
    list_to_permute = list(tuple_to_permute)
    list_to_permute[i], list_to_permute[j] = list_to_permute[j], list_to_permute[i]
    return tuple(list_to_permute)