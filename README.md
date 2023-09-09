# Search_algorithms

## Introduction
This project aims to implement Search algorithms in Python.


## Algorithms

### IDA* Search Algorithm

#### Overview

IDA* (Iterative Deepening A*) is a popular and memory-efficient search algorithm used in artificial intelligence and computer science. It is a variant of the A* search algorithm and was introduced by Richard E. Korf in 1985.

#### Description

IDA* is designed to find the optimal path from a starting node to a goal node in a search space. It combines the advantages of both depth-first search (DFS) and A* search. The key idea behind IDA* is to use a depth-first search approach but with a depth limit, gradually increasing the limit with each iteration until the optimal solution is found.

1. Start with an initial depth limit (usually set to an estimated cost to reach the goal).
2. Perform a depth-first search from the starting node, exploring nodes up to the depth limit.
3. If a goal node is found within the limit, return the solution.
4. If the depth limit is exceeded without finding a goal node, increase the depth limit to the minimum cost of any node that was cutoff during the search.
5. Repeat steps 2-4 until the goal node is found.

IDA* guarantees to find the optimal solution if it exists, and it does so with less memory usage compared to traditional A* search, making it suitable for large search spaces.

#### Reference

The IDA* search algorithm was introduced by Richard E. Korf in the following paper:

- **Title:** "Depth-First Iterative-Deepening: An Optimal Admissible Tree Search" 
- **Author:** Richard E. Korf
- **Year:** 1985
- **Source:** [Link to the paper](https://www.sciencedirect.com/science/article/abs/pii/0004370285900840)



## Domains

The project supports the following domains: 


### N-Puzzle Domain

#### Overview

The N-Puzzle, also known as the sliding puzzle, is a classic puzzle game that has been widely used in the field of search algorithms and artificial intelligence. It serves as an excellent example of a search problem, where the goal is to rearrange a grid of numbered tiles to reach a desired configuration.

#### 15-Puzzle Description

The 15-Puzzle consists of a 4x4 grid with 15 numbered tiles and one empty space. The tiles are initially arranged in a random order within the grid, and the objective is to slide the tiles into the correct numerical order by moving them into the empty space. The puzzle is solved when all tiles are arranged in ascending order from left to right and top to bottom, with the empty space in the bottom-right corner.
