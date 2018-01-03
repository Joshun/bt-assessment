""" 

node_list.py: represents a collection of nodes and enables them to be updated

"""
from __future__ import print_function
from node import Node
from debug_log import print_debug

class NodeList(object):
    def __init__(self):
        self._nodes = {}
        self._nodes_last_update = {}
        

    def _update_node(self, node_name, notification_type, message):
        """ updates a specific node (if necessary) """

        # if node does not exist already, create it
        # if incoming message about node is newer than last state update, update node's state
        if node_name not in self._nodes_last_update or int(message.generated_time) > int(self._nodes_last_update[node_name]):
            self._nodes[node_name] = Node(
                node_name,
                notification_type,
                message
            )
            self._nodes_last_update[node_name] = message.generated_time

            print_debug("Updated node", node_name, "from message", "\"" + message.raw_message + "\"")
        else:
            print_debug("Ignoring message for node", node_name, ":", "\"" + message.raw_message + "\"")

        

    def incoming_message(self, message):
        """ handles an incoming message, updating the relevant nodes accordingly """

        # we know that the node sending the message must be alive
        self._update_node(message.node1_name, "ALIVE", message)

        if message.notification_type == "LOST":
            self._update_node(message.node2_name, "DEAD", message)

        elif message.notification_type == "FOUND":
            self._update_node(message.node2_name, "ALIVE", message)
    
    def print_nodes(self):
        """ prints out the state of all the nodes in NodeList """
        for node_name in self._nodes:
            node = self._nodes[node_name]

            if node.last_message.node2_name == None:
                print(node_name, node.status, node.last_message.receive_time,
                    node.last_message.node1_name, node.last_message.notification_type)
            else:
                print(node_name, node.status, node.last_message.receive_time,
                    node.last_message.node1_name, node.last_message.notification_type, node.last_message.node2_name)
                

