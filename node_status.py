#!/usr/bin/env python2

import sys

from node_exceptions import InvalidLineException
from node_list import NodeList
from message import Message

def show_help():
    print "Usage: node_status.py <input_file.txt>"

def node_status_report(filename):

    node_list = NodeList()

    messages = []

    with open(filename) as f:
        for index, line in enumerate(f):
            try:
                message = Message(line)
                messages.append(message)

            except InvalidLineException:
                print "Error parsing line", index

    for m in messages:
        node_list.incoming_message(m)
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
