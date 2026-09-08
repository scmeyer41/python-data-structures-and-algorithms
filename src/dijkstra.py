"""Dijkstra shortest paths for undirected nonnegative weighted graphs."""

from collections.abc import Iterable
from dataclasses import dataclass
import heapq
from math import inf


@dataclass(frozen=True)
class ShortestPath:
    reachable: bool
    distance: float
    path: tuple[int, ...]


def dijkstra(
    vertex_count: int,
    edges: Iterable[tuple[int, int, float]],
    source: int,
    destination: int,
) -> ShortestPath:
    if vertex_count <= 0:
        raise ValueError("vertex_count must be positive")
    if not 0 <= source < vertex_count or not 0 <= destination < vertex_count:
        raise ValueError("source and destination must be valid vertex indices")

    graph: list[list[tuple[int, float]]] = [[] for _ in range(vertex_count)]
    for left, right, weight in edges:
        if not 0 <= left < vertex_count or not 0 <= right < vertex_count:
            raise ValueError("edge contains an invalid vertex index")
        if weight < 0:
            raise ValueError("Dijkstra's algorithm requires nonnegative weights")
        graph[left].append((right, weight))
        graph[right].append((left, weight))

    distances = [inf] * vertex_count
    parents = [-1] * vertex_count
    distances[source] = 0
    queue = [(0.0, source)]

    while queue:
        current_distance, vertex = heapq.heappop(queue)
        if current_distance != distances[vertex]:
            continue
        if vertex == destination:
            break
        for neighbor, weight in graph[vertex]:
            candidate = current_distance + weight
            if candidate < distances[neighbor]:
                distances[neighbor] = candidate
                parents[neighbor] = vertex
                heapq.heappush(queue, (candidate, neighbor))

    if distances[destination] == inf:
        return ShortestPath(False, inf, ())

    path = []
    current = destination
    while current != -1:
        path.append(current)
        if current == source:
            break
        current = parents[current]
    path.reverse()
    return ShortestPath(True, distances[destination], tuple(path))
