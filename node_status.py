#!/usr/bin/env python2

import sys

from node_exceptions import InvalidLineException
from node_list import NodeList
from message import Message

def show_help():
    print "Usage: node_status.py <input_file.txt>"

def node_status_report(filename):
    # we are processing the file line-by-line instead of reading it all in
    # this is because it is more efficient in terms of storage
    # nodes = {}

    node_list = NodeList()

    with open(filename) as f:
        for index, line in enumerate(f):
            try:
                message = Message(line)
                node_list.incoming_message(message)

            except InvalidLineException:
                print "Error parsing line", index
            # line = line.strip("\n")
            # line = line.split(" ")

            # if len(line) == 4:
            #     receive_time, generated_time, node1, notification_type = line          
            # elif len(line) == 5:
            #     receive_time, generated_time, node1, notification_type, node2 = line
            # else:
            #     print "Error in line", index
    node_list.print_nodes()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Invalid number of arguments."
        show_help()
        sys.exit(1)
    elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
        show_help()
        sys.exit(0)
    else:
        node_status_report(sys.argv[1])
