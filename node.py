"""

node.py: representation of an individual node, including its current state

"""


class Node(object):
    def __init__(self, name, status, last_message):
        self.name = name
        self.status = status
        self.last_message = last_message