# Map Navigation — BFS and A\*

Pathfinding engine implemented in Python that solves **grid-based map navigation problems** using **Breadth-First Search (BFS)** and **A\* Search**. The agent starts at a marked position on the map and must reach the goal using the fewest steps at the lowest cost.

## Problem

Given a 2D grid map with walls, open spaces, a player start position and a goal, find the optimal path from start to goal. Maps follow a Sokoban-inspired format and are loaded from `.txt` files.

### Map legend

| Symbol | Meaning |
|--------|---------|
| `#` | Wall (impassable) |
| `@` | Player start position |
| `x` | Goal |
| `+` | Player on goal |
| `.` | Free space |

## Algorithms implemented

### BFS (Breadth-First Search)
- Guarantees the **shortest path** in terms of number of steps
- Explores all nodes level by level
- No heuristic — blind search

### A\* Search
- Guarantees the **optimal cost path**
- Uses **Manhattan distance** as the heuristic: `|goal_row - row| + |goal_col - col|`
- Expands nodes in order of `f = g + h` (cost so far + estimated cost to goal)

## Technologies

- Python 3
- `collections.deque` — efficient queue for BFS
- `copy.deepcopy` — safe state copying
- `tkinter` — map visualisation (via `libskmaps.py`)

## Project structure

```
MapProblem_24151_24664.py   # Problem definition: state, successors, heuristic
NodeProcura.py              # Search node + BFS and A* implementations
libskmaps.py                # Map I/O and graphical rendering
Mapas/                      # Collection of test map files (.txt)
```

## How to run

**Requirements:** Python 3.x (no external packages needed)

Run directly with a chosen map:
```bash
python NodeProcura.py
```

The default map in `NodeProcura.py` is `./Mapas/begoon59b.txt`. To change it, edit the last lines of the file:
```python
problema = MapProblem("./Mapas/<map_name>.txt")
resultado = NodeProcura.AStar(problema)   # or NodeProcura.BFS(problema)
```

### Output example
```
A visitar: (1, 1)
A visitar: (1, 2)
...
Sequência de ações: ['right', 'right', 'down', ...]
Custo total: 12
Nível do nó: 12
Solução encontrada!
```

## Available maps

The `Mapas/` folder includes a variety of maps, from small grids (`simple.txt`) to large mazes (`maze512-16-0a.txt`), Sokoban puzzles (`Sokoban.txt`), and challenge maps (`impossible.txt`).

## Course

Artificial Intelligence — 2nd year, 2nd semester (2024/2025)
