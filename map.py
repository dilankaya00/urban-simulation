import networkx as nx
import osmnx as ox
from IPython.display import IFrame
from routing import Routing

class FoliumMap:

	def createMap(G):
		# plot the street network with folium
		m = ox.plot_graph_folium(G, weight=2, color="#8b0000")
		return m

	def saveMap(m):
		filepath = "map.html"
		m.save(filepath)
		IFrame(filepath, width=600, height=500)

	def plotPath(G, route):
		# plot the route with folium
		# like above, you can pass keyword args along to folium PolyLine to style the lines
		#print(route)
		m2 = ox.plot_route_folium(G, route, weight=10)
