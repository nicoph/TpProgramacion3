from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class BreadthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:

        node = Node("", state=grid.start, cost=0)

        # Initialize the explored dictionary to be empty
        explored = {} 

        # Initialize the frontier with the initial node
        frontier = QueueFrontier()
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
                if new_state not in explored and not frontier.contains_state(new_state):
                    new_node = Node("", new_state, node.cost + grid.get_cost(new_state))
                    new_node.parent = node
                    new_node.action = action
                    frontier.add(new_node)
