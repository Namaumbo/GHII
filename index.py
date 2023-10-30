
from heapq import heapify, heappush
import sys

# --------------------------------------------------------without classes test function------------------------------------------------------------
# def fun (graph, src, dest):

#     # infinity values for unvisited v
#     inf = sys.maxsize

#     node_data = {
#         "Mchinji":{'cost':inf,'pred':[]},
#         "Kasungu":{'cost':inf,'pred':[]},
#         "Dowa":{'cost':inf,'pred':[]},
#         "Lilongwe":{'cost':inf,'pred':[]},
#         "Ntchisi":{'cost':inf,'pred':[]},
#         "Nkhotakota":{'cost':inf,'pred':[]},
#         'Salima':{'cost':inf,'pred':[]},
#         'Dedza':{'cost':inf,'pred':[]},
#         'Ntcheu':{'cost':inf,'pred':[]}

#                  }
    
#     node_data[src]['cost'] =  0
#     visited = []
#     temp = src

#     for i in range(8):
#         if temp not in visited: 
#             visited.append(temp)
#             min_heap = []
#             for j in graph[temp]:
#                 if j not in visited:
#                     cost  = node_data[temp]['cost'] + graph[temp][j]
#                     if cost < node_data[j]['cost']:
#                         node_data[j]['cost'] = cost
#                         node_data[j]['pred'] = node_data[temp]['pred'] + list(temp)
#                     heappush(min_heap ,(node_data[j]['cost'],j))
#         heapify(min_heap)
#         temp = min_heap[0][1]
#     print(f"short {node_data[dest]['cost']}")
#     print(f"shortest Path {node_data[dest]['pred'] + list(dest)}")


# if __name__ == '__main__':
#     graph ={
#         "Mchinji":{"Kasungu":141 ,"Lilongwe":109},
#         "Kasungu":{"Mchinji":141,"Dowa":117,"Ntchisi":66},
#         "Dowa":{"Kasungu":117, "Ntchisi":38, "Lilongwe":55,"Salima":67},
#         "Lilongwe":{"Mchinji":109,"Dowa":55,"Dedza":92},
#         "Ntchisi":{"Kasungu":66,"Dowa":38,"Nkhotakota":66},
#         "Nkhotakota":{"Ntchisi":66,"Salima":112},
#         "Salima":{"Nkhotakota":112,"Dowa":67,"Dedza":96},
#         "Dedza":{"Lilongwe":92,"Salima":96,"Ntcheu":74},
#         "Ntcheu":{"Dedza":74}
#     }


#     source = 'Mchinji'
#     destination = 'Dowa'
#     fun(graph , source , destination)

#  ------------------------------------ final class based implementation -------------------------
class Graph:

    # G(V,E) v for vertex and E for edge
    def __init__(self):
        # set of empty v
        self.v = {}
        # adding a if the name doesnt exist vertex to the graph
    def add_node(self, name):
        if name not in self.v:
            # initializing and empty point on the graph to hold its info
            self.v[name] = {}
        else:
            print(f"vertex exists in the graph.")
        # adding an edge as well as the weight in this case the cost between the graph vertices
    def add_edge(self, node1, node2, weight):
        # checking if the points exist in the graph
        if node1 in self.v and node2 in self.v:
            self.v[node1][node2] = weight
            self.v[node2][node1] = weight
       

class ShortestPathAvailable:
    def __init__(self, graph):
        self.graph = graph

    # method to calculate the shortest path
    def shortest_path(self, src, dest):
        # for unvisited and unknown V's thats infinity 
        inf = sys.maxsize
        # node_data = {
        #     'Mchinji' :{'cost': inf , 'pred':  []},
        #     'Kasungu' :{'cost': inf , 'pred':  []},
        #     'Dowa' :{'cost': inf , 'pred':  []},
        #     'Lilongwe' :{'cost': inf , 'pred':  []},
        #     'Ntchisi' :{'cost': inf , 'pred':  []},
        #     'Nkhotakota' :{'cost': inf , 'pred':  []},
        #     'Salima' :{'cost': inf , 'pred':  []},
        #     'Ntcheu' :{'cost': inf , 'pred':  []},
        #     'Dedza' :{'cost': inf , 'pred':  []},
        # }
        node_data = {node: {'cost': inf, 'pred': []} for node in self.graph.v}
        node_data[src]['cost'] = 0
        visited = []
        temp = src

        while  temp != dest :
            if temp not in visited:
                visited.append(temp)
                min_heap = []

                for neighbor in self.graph.v[temp]:
                    if neighbor not in visited:
                        cost = node_data[temp]['cost'] + self.graph.v[temp][neighbor]
                        if cost < node_data[neighbor]['cost']:
                            node_data[neighbor]['cost'] = cost
                            node_data[neighbor]['pred'] = node_data[temp]['pred'] + [temp]
                        heappush(min_heap, (node_data[neighbor]['cost'], neighbor))
                if not min_heap:  
                    break 
                heapify(min_heap)
                temp = min_heap[0][1]

               

        shortest_cost = node_data[dest]['cost']
        shortest_path = node_data[dest]['pred'] + [dest]
        return shortest_cost, shortest_path

if __name__ == '__main__':
    # initializing a graph object 
    my_graph = Graph()
    my_graph.add_node('Mchinji')
    my_graph.add_node('Lilongwe')
    my_graph.add_node('Dowa')
    my_graph.add_node('Kasungu')
    my_graph.add_node('Nkhotakota')
    my_graph.add_node('Ntchisi')
    my_graph.add_node('Dedza')
    my_graph.add_node('Salima')
    my_graph.add_node('Ntcheu')
    
    # connectigng the vertex graph we dont only onces since the 
    # connection of to and from weights is taken care by add_edge
    my_graph.add_edge('Mchinji', 'Kasungu', 141)
    my_graph.add_edge('Mchinji', 'Lilongwe', 109)
    my_graph.add_edge('Kasungu', 'Dowa', 117)
    my_graph.add_edge('Kasungu', 'Ntchisi', 66)
    my_graph.add_edge('Dowa', 'Ntchisi',38)
    my_graph.add_edge('Dowa', 'Salima', 67)
    my_graph.add_edge('Dowa', 'Lilongwe', 55)
    my_graph.add_edge('Lilongwe', 'Dedza', 92)
    my_graph.add_edge('Ntchisi', 'Nkhotakota', 66)
    my_graph.add_edge('Nkhotakota', 'Salima', 112)
    my_graph.add_edge('Salima', 'Dedza', 96)
    my_graph.add_edge( 'Dedza','Ntcheu', 74)   

    shortest_path_finder = ShortestPathAvailable(my_graph)


    # --------------------------------------tests cases-------------------------------------
    # 
    #  # Test Case 1: Find the shortest path from Mchinji to Salima
    source_node = 'Mchinji'
    dest_node = 'Salima'
    shortest_cost, path = shortest_path_finder.shortest_path(source_node, dest_node)
    assert shortest_cost == 231
    assert path == ['Mchinji', 'Lilongwe', 'Dowa' , 'Salima']  
    print(f"path_cost: {shortest_cost}")
    print(f"Shortest Path districts: {path}")

    # Test Case 2: Find the shortest path from Mchinji to Ntcheu
    source_node = 'Mchinji'
    dest_node = 'Ntcheu'
    shortest_cost, path = shortest_path_finder.shortest_path(source_node, dest_node)
    assert shortest_cost == 275
    assert path ==  ['Mchinji', 'Lilongwe', 'Dedza', 'Ntcheu']
    print(f"path_cost: {shortest_cost}")
    print(f"Shortest Path districts: {path}")

    # Test Case 3: Find the shortest path from Dowa to Dedza
    source_node = 'Dowa'
    dest_node = 'Dedza'
    shortest_cost, path = shortest_path_finder.shortest_path(source_node, dest_node)
    assert shortest_cost == 147
    assert path ==   ['Dowa', 'Lilongwe', 'Dedza']
    print(f"path_cost: {shortest_cost}")
    print(f"Shortest Path districts: {path}")

 
    print('All tests succeeded! I hope it works on your machine as well','😥'.encode('utf-8'))

    


