from simulator.node import Node


class Distance_Vector_Node(Node):
    def __init__(self, id):
        super().__init__(id)

    # Return a string
    def __str__(self):
        return "Rewrite this function to define your node dump printout"

    # Fill in this function
    def link_has_been_updated(self, neighbor, latency):
        # latency = -1 if delete a link
        pass

    # Fill in this function
    def process_incoming_routing_message(self, m):
        # What to do if you receive message from your neighbors
        pass

    # Return a neighbor, -1 if no path to destination
    def get_next_hop(self, destination):
        # Called by the simulator if simulator wants to get your solution to the routing problems
        # meant to simulate a situation like where you have a "data packet" to send somewhere in the network
        # in order to do that, you have to figure out who to forward it to which of your neighbors.
        # This function, provided "destination" should return the "routing answer"

        return -1
