import unittest
from node_list import NodeList
from message import Message

class TestNodeList(unittest.TestCase):

    def setUp(self):
        self.node_list = NodeList()

    def test_unknown_incoming_message(self):
        message = Message("1508405807560 1508405807504 vader HELLO")
        self.node_list.incoming_message(message)

        self.assertTrue("vader" in self.node_list._nodes)
        self.assertTrue(self.node_list._nodes["vader"].status == "UNKNOWN")
    
    def test_alive_incoming_message(self):
        message = Message("1508405807340 1508405807350 luke HELLO")
        self.node_list.incoming_message(message)

        self.assertTrue("luke" in self.node_list._nodes)
        self.assertTrue(self.node_list._nodes["luke"].status == "ALIVE")
    

if __name__ == "__main__":
    unittest.main()
