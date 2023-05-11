from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


import math

def dist_eucl(state, goal_state):
    x1, y1 = state[0], state[1]
    x2, y2 = goal_state[0], goal_state[1]
    return int(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))

class GreedyBestFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Greedy Best First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node("", grid.start, 0)

        # Initialize the explored dictionary to be empty
        explored = {} 
        
        # Add the node to the explored dictionary
        explored[node.state] = True

        frontier = PriorityQueueFrontier()
        frontier.add(node, dist_eucl(node.state, grid.end))
        print(frontier)

        while True:

            # Check if there are no more nodes in the frontier
            if frontier.is_empty():
                return NoSolution(explored)

            # Remove the next node from the frontier
            node = frontier.pop()
            print(node)
            # Mark the node as explored
            explored[node.state] = True

            # Check if we have reached the goal state
            if node.state == grid.end:
                return Solution(node, explored)

            # Explore the neighbors of the current node
            neighbours = grid.get_neighbours(node.state)
            for action, new_state in neighbours.items():
                print(frontier.contains_state(new_state))
            for action, new_state in neighbours.items():                
                if new_state not in explored and not frontier.contains_state(new_state) :
                    new_node = Node("", new_state, node.cost + grid.get_cost(new_state))
                    new_node.parent = node
                    new_node.action = action
                    frontier.add(new_node, dist_eucl(new_node.state, grid.end))

        
