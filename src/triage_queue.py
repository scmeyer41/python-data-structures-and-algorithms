"""Linked-list queue with a critical-patient priority rule."""

from dataclasses import dataclass


@dataclass
class PatientNode:
    name: str
    severity: int
    next: "PatientNode | None" = None


class TriageQueue:
    """FIFO queue where severity-5 patients move ahead of severities 1-4.

    Severity-5 patients remain FIFO relative to other severity-5 patients.
    All other patients remain FIFO relative to one another.
    """

    def __init__(self) -> None:
        self.head: PatientNode | None = None
        self.current_length = 0
        self.max_length = 0
        self.served_count = {severity: 0 for severity in range(1, 6)}

    def arrive(self, name: str, severity: int) -> None:
        if not name.strip():
            raise ValueError("name must not be empty")
        if severity not in range(1, 6):
            raise ValueError("severity must be between 1 and 5")

        new_node = PatientNode(name.strip(), severity)
        if self.head is None:
            self.head = new_node
        elif severity == 5:
            previous = None
            current = self.head
            while current is not None and current.severity == 5:
                previous, current = current, current.next
            if previous is None:
                new_node.next = self.head
                self.head = new_node
            else:
                new_node.next = current
                previous.next = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

        self.current_length += 1
        self.max_length = max(self.max_length, self.current_length)

    def call_next(self) -> tuple[str, int] | None:
        if self.head is None:
            return None
        patient = self.head
        self.head = patient.next
        self.current_length -= 1
        self.served_count[patient.severity] += 1
        return patient.name, patient.severity

    def remove(self, name: str) -> bool:
        previous = None
        current = self.head
        while current is not None:
            if current.name == name:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                self.current_length -= 1
                return True
            previous, current = current, current.next
        return False

    def waiting_list(self) -> list[tuple[str, int]]:
        patients = []
        current = self.head
        while current is not None:
            patients.append((current.name, current.severity))
            current = current.next
        return patients

    def metrics(self) -> dict:
        return {
            "current_length": self.current_length,
            "maximum_length": self.max_length,
            "served_by_severity": self.served_count.copy(),
        }
