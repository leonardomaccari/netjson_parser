import json 
import networkx as nx

def load_network(json_file):
    """ import a json file in NetJSON format, convert to Graph class
    Parameters
    ----------
    json_file : string with file path
    """

    try:
        file_p = open(json_file, "r")
    except IOError:
        raise
    try:
        netjson_net = json.load(file_p)
    except ValueError as err:
        print "Could not decode file", err
    # TODO add a schema to validate the subset of features we are
    # able to consider

    G = nx.Graph()
    cost_label = ""
    if "metric" in netjson_net and netjson_net["metric"] == "ETX":
        cost_label = "cost"
    for node in netjson_net["nodes"]:
        G.add_node(node["id"])
    for link in netjson_net["links"]:
        if cost_label:
            cost = float(link["cost"])
        else:
            cost = 1.0
        G.add_edge(link["source"], link["target"],
                   {"weight": cost})
    return G





