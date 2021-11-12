import numpy as np
import osmnx as ox

class Routing:

	def findShortestPath(G, first, last):
		# find the shortest path (by distance) between these nodes then plot it
		origNode = list(G)[first]
		destNode = list(G)[last]
		route = ox.shortest_path(G, origNode, destNode, weight="length")
		return route

	def plotShortestPath(route, G):
		fig, ax = ox.plot_graph_route(G, route, route_color="r", route_linewidth=6, node_size=0)

	def speedAndTime(G, origNode, destNode):
		# impute speed on all edges missing data
		G = ox.add_edge_speeds(G)
		# calculate travel time (seconds) for all edges
		G = ox.add_edge_travel_times(G)

		# calculate two routes by minimizing travel distance vs travel time
		orig = list(G)[origNode]
		dest = list(G)[destNode]
		route1 = ox.shortest_path(G, orig, dest, weight="length")
		route2 = ox.shortest_path(G, orig, dest, weight="travel_time")
		# plot the routes
		fig, ax = ox.plot_graph_routes(G, routes=[route1, route2], route_colors=["r", "y"], route_linewidth=6, node_size=0)

		# compare the two routes
		route1_length = int(sum(ox.utils_graph.get_route_edge_attributes(G, route1, "length")))
		route2_length = int(sum(ox.utils_graph.get_route_edge_attributes(G, route2, "length")))
		route1_time = int(sum(ox.utils_graph.get_route_edge_attributes(G, route1, "travel_time")))
		route2_time = int(sum(ox.utils_graph.get_route_edge_attributes(G, route2, "travel_time")))
		print("Route 1 is", route1_length, "meters and takes", route1_time, "seconds.")
		print("Route 2 is", route2_length, "meters and takes", route2_time, "seconds.")








