from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node

class UniformCostSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using A* Search

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
        frontier.add(node, node.cost )
        
        while True:

            # Check if there are no more nodes in the frontier
            if frontier.is_empty():
                return NoSolution(explored)

            # Remove the next node from the frontier
            node = frontier.pop()
            
            # Mark the node as explored
            explored[node.state] = True

            # Check if we have reached the goal state
            if node.state == grid.end:
                return Solution(node, explored)

            # Explore the neighbors of the current node
            neighbours = grid.get_neighbours(node.state)
            for action, new_state in neighbours.items():   
                #nombre = str(randint(1,100))
                new_node = Node("",new_state, node.cost + grid.get_cost(new_state))
                new_node.parent = node
                new_node.action = action     
                if new_node.state not in explored or  new_node.cost < grid.get_cost(new_node.state):#frontier.contains_state__with_cost(new_state) :
                    frontier.add(new_node,new_node.cost)