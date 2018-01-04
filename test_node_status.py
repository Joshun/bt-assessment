import unittest
from node_list import NodeList
from message import Message

class TestNodeList(unittest.TestCase):

    def setUp(self):
        self.node_list = NodeList()

    def test_hello_incoming_message(self):
        message = Message("1508405807340 1508405807350 luke HELLO")
        self.node_list.incoming_message(message)

        self.assertIn("luke", self.node_list._nodes)
        self.assertEqual(self.node_list._nodes["luke"].status, "ALIVE")
    

    def test_lost_incoming_message(self):
        message = Message("1508405807512 1508405807500 vader LOST luke")
        self.node_list.incoming_message(message)

        self.assertIn("luke", self.node_list._nodes)
        self.assertEqual(self.node_list._nodes["luke"].status, "DEAD")
        self.assertEqual(self.node_list._nodes["vader"].status, "ALIVE")
    
    
    def test_found_incoming_message(self):
        message = Message("1508405807467 1508405807479 luke FOUND r2d2")
        self.node_list.incoming_message(message)

        self.assertIn("r2d2", self.node_list._nodes)
        self.assertEqual(self.node_list._nodes["r2d2"].status, "ALIVE")
        self.assertEqual(self.node_list._nodes["luke"].status, "ALIVE")
        


if __name__ == "__main__":
    unittest.main()
