#! /usr/bin/env python2
import netjson
import argparse
import os
import networkx as nx


def main():
    choices = ["edgelist", "graphml", "gpickle"]
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', dest="inputfile", help="The input NetJSON file",
                        required=True)
    parser.add_argument('-t', dest="type", choices=choices,
                        help="The kind of output file", required=True)
    parser.add_argument('-o', dest="outputfile", help="The output file")

    args = parser.parse_args()

    if args.outputfile:
        outputfile = args.outputfile
    else:
        outputfile = os.path.splitext(args.inputfile)[0] + "." + args.type

    g = netjson.load_network(args.inputfile)

    write_function = getattr(nx, "write_" + args.type)
    write_function(g, outputfile)


if __name__ == "__main__":
    main()
