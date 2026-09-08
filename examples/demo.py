import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from binary_search_tree import BinarySearchTree
from dijkstra import dijkstra
from triage_queue import TriageQueue


def main() -> None:
    tree = BinarySearchTree()
    for value in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
        tree.insert(value)
    print("BST inorder:", tree.inorder())

    queue = TriageQueue()
    queue.arrive("Alex", 2)
    queue.arrive("Jordan", 5)
    queue.arrive("Morgan", 3)
    print("Triage order:", queue.waiting_list())

    result = dijkstra(
        5,
        [(0, 1, 4), (0, 2, 1), (2, 1, 2), (1, 3, 1), (3, 4, 3)],
        0,
        4,
    )
    print("Shortest path:", result)


if __name__ == "__main__":
    main()
