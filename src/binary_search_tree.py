"""Recursive binary search tree for distinct integer values."""

from dataclasses import dataclass


@dataclass
class Node:
    value: int
    left: "Node | None" = None
    right: "Node | None" = None


class BinarySearchTree:
    def __init__(self) -> None:
        self.root: Node | None = None

    def insert(self, value: int) -> bool:
        self.root, inserted = self._insert(self.root, value)
        return inserted

    def _insert(self, node: Node | None, value: int) -> tuple[Node, bool]:
        if node is None:
            return Node(value), True
        if value < node.value:
            node.left, inserted = self._insert(node.left, value)
            return node, inserted
        if value > node.value:
            node.right, inserted = self._insert(node.right, value)
            return node, inserted
        return node, False

    def search(self, value: int) -> bool:
        current = self.root
        while current is not None:
            if value == current.value:
                return True
            current = current.left if value < current.value else current.right
        return False

    def delete(self, value: int) -> bool:
        self.root, deleted = self._delete(self.root, value)
        return deleted

    def _delete(self, node: Node | None, value: int) -> tuple[Node | None, bool]:
        if node is None:
            return None, False
        if value < node.value:
            node.left, deleted = self._delete(node.left, value)
            return node, deleted
        if value > node.value:
            node.right, deleted = self._delete(node.right, value)
            return node, deleted

        if node.left is None:
            return node.right, True
        if node.right is None:
            return node.left, True

        successor = self._minimum(node.right)
        node.value = successor.value
        node.right, _ = self._delete(node.right, successor.value)
        return node, True

    @staticmethod
    def _minimum(node: Node) -> Node:
        while node.left is not None:
            node = node.left
        return node

    def inorder(self) -> list[int]:
        values: list[int] = []

        def visit(node: Node | None) -> None:
            if node is not None:
                visit(node.left)
                values.append(node.value)
                visit(node.right)

        visit(self.root)
        return values

    def preorder(self) -> list[int]:
        values: list[int] = []

        def visit(node: Node | None) -> None:
            if node is not None:
                values.append(node.value)
                visit(node.left)
                visit(node.right)

        visit(self.root)
        return values

    def postorder(self) -> list[int]:
        values: list[int] = []

        def visit(node: Node | None) -> None:
            if node is not None:
                visit(node.left)
                visit(node.right)
                values.append(node.value)

        visit(self.root)
        return values

    def height(self) -> int:
        """Return height measured in edges; an empty tree has height -1."""

        def measure(node: Node | None) -> int:
            if node is None:
                return -1
            return 1 + max(measure(node.left), measure(node.right))

        return measure(self.root)
