from node_exceptions import InvalidLineException

class Message(object):
    def __init__(self, raw_line):
        line = raw_line.strip("\n")
        split_line = line.split(" ")
        
        if len(split_line) != 4 and len(split_line) != 5:
            raise InvalidLineException("invalid line length")
        
        self.raw_message = line
        self.receive_time = split_line[0]
        self.generated_time = split_line[1]
        self.node1_name = split_line[2]        
        self.notification_type = split_line[3]
        self.node2_name = split_line[4] if len(split_line) == 5 else None

        if self.notification_type not in ["HELLO", "LOST", "FOUND"]:
            raise InvalidLineException("invalid message type")
