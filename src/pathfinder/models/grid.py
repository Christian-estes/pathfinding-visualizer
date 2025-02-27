from .node import Node 

class Grid:
    def __init__(
        self,
        grid: list[list[Node]],
        start: tuple[int, int],
        end: tuple[int, int]
    ) -> None:
        self.grid = grid 
        self.start = start 
        self.end = end

        # calculate grid dimensions
        self.height = len(grid)
        self.width = max(len(row) for row in grid)
    
    def get_node(self, pos: tuple[int, int]) -> Node:
        return self.grid[pos[0]][pos[1]]

    def get_cost(self, pos: tuple[int, int]) -> int:
        return self.grid[pos[0]][pos[1]].cost

    def get_neighbors(self, pos: tuple[int, int]) -> dict[str, tuple[int, int]]:
        """Determine the neighbors of a cell

        Args:
            pos (tuple[int, int]): Cell position

        Returns:
            dict[str, tuple[int, int]]: Action - Position mapper
        """
        row, col = pos 

        # Map actions with resulting cell positions
        action_pos_mapper = {
            "up": (row - 1, col),
            "down": (row + 1, col),
            "left": (row, col - 1),
            "right": (row, col + 1)
        }

        # Determine the possible actions
        possible_actions = {}

        for action, (r, c) in action_pos_mapper.items():
            if not (0 <= r < self.height and 0 <= c < self.width):
                continue 
                
            if self.grid[r][c].value == '#':
                continue 
            
            possible_actions[action] = (r, c) 
        
        return possible_actions

    def __repr__(self) -> str:
        return f"Grid([[...], ...], {self.start}, {self.end})"
            