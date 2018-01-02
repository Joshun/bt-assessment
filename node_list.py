from __future__ import print_function
from node import Node
from debug_log import print_debug

class NodeList(object):
    def __init__(self):
        self._nodes = {}
        self._nodes_last_update = {}
        

    def _update_node(self, node_name, notification_type, message):
        if node_name not in self._nodes_last_update or int(message.receive_time) > int(self._nodes_last_update[node_name]):
            self._nodes[node_name] = Node(
                node_name,
                notification_type,
                message
            )
            self._nodes_last_update[node_name] = message.receive_time

            print_debug("Updated node", node_name, "from message", "\"" + message.raw_message + "\"")
        else:
            print_debug("Ignoring message for node", node_name, ":", "\"" + message.raw_message + "\"")

        

    def incoming_message(self, message):
        # we know that the node sending the message must be alive
        self._update_node(message.node1_name, "ALIVE", message)

        if message.notification_type == "LOST":
            self._update_node(message.node2_name, "DEAD", message)

        elif message.notification_type == "FOUND":
            self._update_node(message.node2_name, "ALIVE", message)
    
    def print_nodes(self):
        for node_name in self._nodes:
            node = self._nodes[node_name]

            if node.last_message.node2_name == None:
                print(node_name, node.status, node.last_message.receive_time,
                    node.last_message.node1_name, node.last_message.notification_type)
            else:
                print(node_name, node.status, node.last_message.receive_time,
                    node.last_message.node1_name, node.last_message.notification_type, node.last_message.node2_name)
                

