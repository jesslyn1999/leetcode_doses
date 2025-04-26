from collections import deque
from typing import List

def min_cost_collect_balls(m: int, n: int, position: int, table: List[int]) -> int:
    """
    Find the minimum cost to collect all types of balls.
    
    Args:
        m: Number of positions in the table
        n: Number of ball types to collect
        position: Starting position (1-indexed)
        table: Array representing the ball types at each position (1-indexed)
    
    Returns:
        Minimum total cost to collect all required balls
    """
    # Convert position to 0-indexed for easier array manipulation
    position = position - 1
    
    # Create a set of ball types that need to be collected
    required_balls = set(range(1, n+1))
    
    # Use BFS to find the minimum cost
    queue = deque([(position, 0, set())])  # (position, cost, collected_balls)
    visited = set([(position, frozenset())])  # (position, frozenset of collected_balls)
    
    while queue:
        pos, cost, collected = queue.popleft()
        
        # If position is valid, collect the ball at current position
        if 0 <= pos < m:
            ball_type = table[pos]
            new_collected = collected.copy()
            if ball_type in required_balls:
                new_collected.add(ball_type)
            
            # Check if we've collected all required balls
            if len(new_collected) == n:
                return cost
            
            # Convert to frozenset for hashing in the visited set
            collected_frozen = frozenset(new_collected)
            
            # Try moving left
            if (pos-1, collected_frozen) not in visited:
                visited.add((pos-1, collected_frozen))
                queue.append((pos-1, cost+1, new_collected))
            
            # Try moving right
            if (pos+1, collected_frozen) not in visited:
                visited.add((pos+1, collected_frozen))
                queue.append((pos+1, cost+1, new_collected))
    
    return -1  # If it's impossible to collect all ball types

def main():
    # Example from the problem
    m = 7
    n = 6
    position = 4
    table = [1, 2, 1, 3, 4, 5, 6]
    
    # Call the function and print the result
    result = min_cost_collect_balls(m, n, position, table)
    print(f"Minimum cost: {result}")
    
    # Custom test case
    m2 = 7
    n2 = 6
    position2 = 4
    table2 = [1, 2, 1, 3, 4, 5, 6]
    
    result2 = min_cost_collect_balls(m2, n2, position2, table2)
    print(f"Minimum cost for second example: {result2}")

if __name__ == "__main__":
    main()
