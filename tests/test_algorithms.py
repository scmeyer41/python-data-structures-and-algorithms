import sys
import unittest
from math import inf
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from binary_search_tree import BinarySearchTree
from dijkstra import dijkstra
from triage_queue import TriageQueue


class TriageQueueTests(unittest.TestCase):
    def test_critical_patients_move_ahead_and_remain_fifo(self):
        queue = TriageQueue()
        queue.arrive("A", 2)
        queue.arrive("B", 5)
        queue.arrive("C", 5)
        queue.arrive("D", 3)
        self.assertEqual(queue.waiting_list(), [("B", 5), ("C", 5), ("A", 2), ("D", 3)])

    def test_remove_and_metrics(self):
        queue = TriageQueue()
        queue.arrive("A", 1)
        queue.arrive("B", 5)
        self.assertTrue(queue.remove("A"))
        self.assertEqual(queue.call_next(), ("B", 5))
        self.assertEqual(queue.metrics()["served_by_severity"][5], 1)


class BinarySearchTreeTests(unittest.TestCase):
    def setUp(self):
        self.tree = BinarySearchTree()
        for value in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
            self.tree.insert(value)

    def test_traversals_and_height(self):
        self.assertEqual(self.tree.inorder(), [1, 3, 4, 6, 7, 8, 10, 13, 14])
        self.assertEqual(self.tree.height(), 3)
        self.assertTrue(self.tree.search(7))
        self.assertFalse(self.tree.search(2))

    def test_delete_leaf_one_child_two_children_and_root(self):
        for value in [1, 14, 3, 8]:
            self.assertTrue(self.tree.delete(value))
        self.assertEqual(self.tree.inorder(), [4, 6, 7, 10, 13])

    def test_duplicate_is_ignored(self):
        self.assertFalse(self.tree.insert(8))


class DijkstraTests(unittest.TestCase):
    def test_shortest_path(self):
        result = dijkstra(5, [(0, 1, 4), (0, 2, 1), (2, 1, 2), (1, 3, 1), (3, 4, 3)], 0, 4)
        self.assertTrue(result.reachable)
        self.assertEqual(result.distance, 7)
        self.assertEqual(result.path, (0, 2, 1, 3, 4))

    def test_unreachable_destination(self):
        result = dijkstra(4, [(0, 1, 3)], 0, 3)
        self.assertFalse(result.reachable)
        self.assertEqual(result.distance, inf)
        self.assertEqual(result.path, ())

    def test_negative_weight_is_rejected(self):
        with self.assertRaises(ValueError):
            dijkstra(2, [(0, 1, -1)], 0, 1)


if __name__ == "__main__":
    unittest.main()
