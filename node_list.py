from node import Node

class NodeList(object):
    def __init__(self):
        self._nodes = {}
    def incoming_message(self, message):
        # we know that the node sending the message must be alive
        self._nodes[message.node1_name] = Node(
            message.node1_name,
            "ALIVE",
            message
        )

        if message.notification_type == "LOST":
            self._nodes[message.node2_name] = Node(
                message.node2_name,
                "DEAD",
                message
            )
        elif message.notification_type == "FOUND":
            self._nodes[message.node2_name] = Node(
                message.node2_name,
                "ALIVE",
                message
            )
    
    def print_nodes(self):
        for node_name in self._nodes:
            node = self._nodes[node_name]

            if node.last_message.node2_name == None:
                print node_name, node.status, node.last_message.receive_time, node.last_message.node1_name, node.last_message.notification_type
            else:
                print node_name, node.status, node.last_message.receive_time, node.last_message.node1_name, node.last_message.notification_type, node.last_message.node2_name
                

