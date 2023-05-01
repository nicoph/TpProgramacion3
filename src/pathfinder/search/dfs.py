from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search

        Args:
            grid (Grid): Grid of points
            
        Returns:
            Solution: Solution found
        """
        node = Node("", state=grid.start, cost=0)

        # Initialize the explored dictionary to be empty
        explored = {}

        # Initialize the frontier with the initial node
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

            # Iterar los vecinos en orden inverso porque usa pila en vez de cola
            for action, new_state in reversed(list(neighbours.items())):
                if new_state not in explored and not frontier.contains_state(new_state):
                    new_node = Node("", new_state, node.cost + grid.get_cost(new_state))
                    new_node.parent = node
                    new_node.action = action
                    frontier.add(new_node)
