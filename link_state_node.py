from simulator.node import Node
import json



class Link_State_Node(Node):
    def __init__(self, id):
        super().__init__(id)
        # What does a node (ID) need. ID is unique and represents speciifc node
        # store all the link_cost/edge information
        # Remember all the traffic i sent
        # EVENTS: ADD_LINK: src, dst ,latency
        # What makes them unique: link src, link dst, seq number
        # link src= id
        # seq number?
        # each node needs to remember all traffic it sent
        #geeksforgeeks.org/generate-graph-using-dictionary/python/
        # KEYS = self.ID (keys are the nodes of the graph)
        # Value = list of neighbors
        self.seq = {self.id : 0}
        self.graph = {}
        self.graph[self.id] = {"seq": self.seq}
        self.remember = {"traffic":[]}
        self.seq = {self.id : }
        self.node = id


        #need Src, Dst, Cost, SEq#

    # Return a string
    # Whenever DUMP_NODE, it calls the str(node) to print whatever is implemented in __str__() method
    def __str__(self):
        return "Rewrite this function to define your node dump printout"

    # Fill in this function
    # Latency is the COST
    def link_has_been_updated(self, neighbor, latency):
        # latency = -1 if delete a link
        if latency == -1 and neighbor in self.neighbors: # This is from generic_node.py
            self.neighbors.remove(neighbor)
        #
        pass

    # Fill in this function
    def process_incoming_routing_message(self, m):
        pass

    # Return a neighbor, -1 if no path to destination
    def get_next_hop(self, destination):
        # Run djikstra's algorithm
        return -1
