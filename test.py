from geo import Network
from routing import Routing
from map import FoliumMap
import warnings

warnings.filterwarnings("ignore")

west = 27.8001
east = 27.8652
south = 37.8139
north = 37.8643

n = Network.createNetwork(west, east, south, north)
n = Network.simplifyNetwork(n)
#Network.plotNetwork(n)
#Network.saveNetwork(n)

origNode = 50
destNode = 60
route = Routing.findShortestPath(n, origNode, destNode)
#Routing.plotShortestPath(route, n)
#Routing.speedAndTime(n, origNode, destNode)

m = FoliumMap.createMap(n)
FoliumMap.plotPath(n, route)
FoliumMap.saveMap(m)