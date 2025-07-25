# -*- coding: utf-8 -*-
"""
1. Add the aStarSearch and functionHeuristic methods to the Puzzle class.
2. Call this new method to test its implementation in main file.
"""
##-----------------------------------------------------------------------------
##setting up the puzzle
##----------------------------------------------------------------------------- 
class Puzzle:
    def __init__(self):
        self.initial_state = ['1', '2', '3', '5', '6', '8', '4', '0', '7']
        self.goal_state = ['1', '2', '3', '4', '5', '6', '7', '8', '0']
        self.visited_states = []

    def print_puzzle(self, state):
        for i in range(0, 9, 3):
            print(state[i:i+3])

    def get_blank_position(self, state):
        return state.index('0')

    def get_possible_moves(self, state):
        blank_index = self.get_blank_position(state)
        moves = []
        if blank_index % 3 != 0: # Move left
            moves.append(-1)
        if blank_index % 3 != 2: # Move right
            moves.append(1)
        if blank_index > 2: # Move up
            moves.append(-3)
        if blank_index < 6: # Move down
            moves.append(3)
        return moves

    def apply_move(self, state, move):
        new_state = state[:]
        blank_index = self.get_blank_position(new_state)
        swap_index = blank_index + move
        new_state[blank_index], new_state[swap_index] = new_state[swap_index], new_state[blank_index]
        return new_state

    def calculate_manhattan_distance(self, state):
        distance = 0
        for i in range(9):
            if state[i] != '0':
                tile_value = int(state[i])
                goal_index = self.goal_state.index(state[i])
                current_row, current_col = divmod(i, 3)
                goal_row, goal_col = divmod(goal_index, 3)
                distance += abs(current_row - goal_row) + abs(current_col - goal_col)
        return distance

    def functionHeuristic(self, state, cost):
        """
        Calculates f(n) = h(n) + g(n)
        h(n): Manhattan distance
        g(n): cost to reach the node
        """
        return self.calculate_manhattan_distance(state) + cost

    def aStarSearch(self):
        """
        Performs A* search to find the optimal solution.
        """
        print("A* SEARCH")
        print("____________________________________________________________")

        open_list = [(self.initial_state, 0, self.functionHeuristic(self.initial_state, 0), [self.initial_state])] # (state, cost, f(n), path)
        self.visited_states = []

        while open_list:
            open_list.sort(key=lambda x: x[2]) # Sort by f(n)
            current_state, current_cost, current_f, current_path = open_list.pop(0)

            if current_state == self.goal_state:
                print("\n ------------------------------------------------------------")
                print("Initial State: ", self.initial_state)
                print("Goal State: ", self.goal_state)
                print("Path: ", current_path)
                print("Solution Found!")
                return current_path

            if current_state in self.visited_states:
                continue

            self.visited_states.append(current_state)

            possible_moves = self.get_possible_moves(current_state)

            for move in possible_moves:
                new_state = self.apply_move(current_state, move)
                new_cost = current_cost + 1
                new_f = self.functionHeuristic(new_state, new_cost)
                new_path = current_path + [new_state]

                # Check if the new state is already in the open list with a higher f(n)
                found_in_open = False
                for i, (state, cost, f, path) in enumerate(open_list):
                    if state == new_state and f <= new_f:
                        found_in_open = True
                        break

                if not found_in_open and new_state not in self.visited_states:
                     open_list.append((new_state, new_cost, new_f, new_path))

        print("\n ------------------------------------------------------------")
        print("Initial State: ", self.initial_state)
        print("Goal State: ", self.goal_state)
        print("No solution found.")
        return None

    def simpleHillClimbing(self):
        """
        Performs simple hill climbing search.
        """
        print("SIMPLE HILL CLIMBING")
        print("____________________________________________________________")

        current_state = self.initial_state
        current_h = self.calculate_manhattan_distance(current_state)
        path = [current_state]
        level = 0
        self.visited_states = []

        while current_h > 0:
            print(f"\n---------")
            print(f"LEVEL  {level}")
            print(f"---------")
            print(f"        CURRENT NODE: ", current_state, current_h)
            self.visited_states.append(current_state)

            possible_moves = self.get_possible_moves(current_state)
            next_states = []

            for move in possible_moves:
                new_state = self.apply_move(current_state, move)
                new_h = self.calculate_manhattan_distance(new_state)
                next_states.append((new_state, new_h))

            next_states.sort(key=lambda x: x[1]) # Sort by heuristic value
            print(f"        OPEN LIST: ", next_states)

            best_next_state, best_next_h = next_states[0]

            if best_next_h < current_h and best_next_state not in self.visited_states:
                current_state = best_next_state
                current_h = best_next_h
                path.append(current_state)
                level += 1
                print("selected: ", current_state, current_h)
            else:
                print("there is no better move or already visited")
                print("\n ------------------------------------------------------------")
                print("Initial State: ", self.initial_state)
                print("Goal State: ", self.goal_state)
                print("Path: ", path)
                print("LOCAL MAXIMUM: There is no solution")
                return None

        print("\n ------------------------------------------------------------")
        print("Initial State: ", self.initial_state)
        print("Goal State: ", self.goal_state)
        print("Path: ", path)
        print("Solution Found!")
        return path