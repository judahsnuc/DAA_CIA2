from aco_routing.utils.graph import Graph
from aco_routing.dijkstra import Dijkstra
from aco_routing.utils.simulator import Simulator
from aco_routing.aco import ACO

graph = Graph()

graph.add_edge("A", "B", travel_time=2)
graph.add_edge("B", "C", travel_time=2)
graph.add_edge("A", "H", travel_time=2)
graph.add_edge("H", "G", travel_time=2)
graph.add_edge("C", "F", travel_time=1)
graph.add_edge("F", "G", travel_time=1)
graph.add_edge("G", "F", travel_time=1)
graph.add_edge("F", "C", travel_time=1)
graph.add_edge("C", "D", travel_time=10)
graph.add_edge("E", "D", travel_time=2)
graph.add_edge("G", "E", travel_time=2)

source = "A"
destination = "D"

aco = ACO(graph)
dijkstra = Dijkstra(graph)

dijkstra_path, dijkstra_cost = dijkstra.find_shortest_path(source, destination)
aco_path, aco_cost = aco.find_shortest_path(source, destination)

print(f"ACO - path: {aco_path}, cost: {aco_cost}")
print(f"Dijkstra - path: {dijkstra_path}, cost: {dijkstra_cost}")

Simulator(graph).simulate(source, destination, num_episodes=100, plot=True)