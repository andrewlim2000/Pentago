b = branching factor
d = depth level
p = number of nodes at previous level

Minimax Algorithm:

Number of nodes expanded: At each depth level: (36 - d + 1) * 8 * p
Depth level for look-ahead: 2
Time complexity: O(bd)
Space complexity: O(b^d)
Number of nodes expanded at depth level 1 = 36 * 8 = 288
Number of nodes expanded at depth level 2 = 35 * 8 * 288 = 80640

Minimax with Alpha-Beta Pruning:

Number of nodes expanded: Depends on player moves and utility function.
Depth level for look-ahead: 2. Generating a tree of depth level 4 still took too long even with pruning.
Time complexity: O(b^(d/2))
Space complexity: O(bd)
Number of nodes expanded at depth level 1: Depends on player moves and utility function.
Number of nodes expanded at depth level 2: Depends on player moves and utility function.