from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class UniformCostSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Uniform Cost Search

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

        frontier = StackFrontier()
        frontier.add(node)

        # Initialize the visited matrix to False for all nodes
        visited = [[False] * grid.width for _ in range(grid.height)]

        while True:

            # caso base
            if frontier.is_empty():
                return NoSolution(explored)

            # sacar nodo de frontera
            node = frontier.remove()

            # poner explorado
            explored[node.state] = True

            # caso base
            if node.state == grid.end:
                return Solution(node, explored)

            # ir añadiendo moviendo de a uno
            neighbours = grid.get_neighbours(node.state)
            for action, new_state in neighbours.items():
                if not explored.get(new_state):
                    new_node = Node("", new_state, node.cost + grid.get_cost(new_state))
                    new_node.parent = node
                    new_node.action = action
                    frontier.add(new_node)
                elif frontier.contains_state(new_state):
                    for frontier_node in frontier.frontier:
                        if frontier_node.state == new_state and frontier_node.cost > node.cost + grid.get_cost(new_state):
                            frontier_node.cost = node.cost + grid.get_cost(new_state)
                            frontier_node.parent = node
                            frontier_node.action = action
                            break
        
