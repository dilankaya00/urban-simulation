# west = 27.8001
# east = 27.8652
# south = 37.8139
# north = 37.8643

import networkx as nx
import osmnx as ox

class Network:

	def createNetwork(west, east, south, north):
		G = ox.graph_from_bbox(north, south, east, west, network_type="drive_service", simplify=False)
		#Gp = ox.project_graph(G)
		return G

	def simplifyNetwork(G):
		G = ox.simplify_graph(G)
		return G

	def plotNetwork(G):
		ec = ox.plot.get_edge_colors_by_attr(G, attr="length", cmap="plasma_r")
		fig, ax = ox.plot_graph(G, node_color="w", node_edgecolor="k", node_size=20, edge_color=ec, edge_linewidth=3)

	def saveNetwork(G):
		ox.save_graphml(G, filepath="network.graphml")

