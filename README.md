# Python Data Structures and Algorithms

Three from-scratch Python implementations developed for CS 610 Data Structures and Algorithms: a linked-list triage queue, a binary search tree, and Dijkstra's shortest-path algorithm.

The original coursework was completed individually by Steven Meyer. The implementations were subsequently reorganized into reusable modules and supplemented with automated tests for this portfolio repository.

## Implementations

| Module | Capabilities | Principal complexity |
|---|---|---|
| Triage queue | Arrival, removal, service order, and queue metrics | Arrival is O(n); service is O(1) |
| Binary search tree | Insert, search, delete, height, and three traversals | Average O(log n); worst-case O(n) |
| Dijkstra | Shortest distance and reconstructed path | O((V + E) log V) with an adjacency list and heap |

## Triage queue

The queue uses a singly linked list and follows the original assignment's critical-patient rule. Severity-5 patients move ahead of severities 1-4 while remaining FIFO relative to other severity-5 patients. Patients in severities 1-4 remain FIFO relative to one another.

This is intentionally not described as a complete five-level priority queue because severities 1-4 are not mutually reordered.

## Binary search tree

The BST supports recursive insertion and deletion, iterative searching, inorder/preorder/postorder traversal, and height calculation. Deletion handles leaves, nodes with one child, and nodes with two children using the inorder successor. Duplicate values are ignored.

## Dijkstra shortest path

The graph implementation uses an adjacency list and `heapq`. It supports undirected graphs with nonnegative weights, terminates when the destination is finalized, and reconstructs the path through parent pointers. Invalid vertices and negative weights are rejected explicitly.

## Repository structure

```text
.
├── README.md
├── requirements.txt
├── src/
│   ├── triage_queue.py
│   ├── binary_search_tree.py
│   └── dijkstra.py
├── examples/
│   └── demo.py
└── tests/
    └── test_algorithms.py
```

## Run the demonstration

Python 3.10 or newer is recommended. No third-party packages are required.

```bash
python examples/demo.py
```

## Run the tests

```bash
python -m unittest discover -s tests -v
```

The tests cover priority ordering, queue removal and metrics, BST traversal and each deletion case, duplicate insertion, shortest-path reconstruction, unreachable vertices, and negative-edge rejection.

## Portfolio refactoring

The original assignments included interactive Colab interfaces and script-oriented input handling. For this repository, the core algorithms were separated from their interfaces, filenames were standardized, validation was made explicit, and tests were added. These changes improve reuse and maintainability while preserving the original algorithmic behavior.
