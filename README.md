# netjson_parser

This is a simple library and a main file that reads the input in the [NetJSON](http://netjson.org) format (a format imagined to describe networks) and saves it in another format using the networkX library.

Right now the edgelist, graphm and gpickle output format are supported, but you can add more formats modifying the "choices" variable in the main file. If you add the "foo" format to the list, and there is a networkx function called "write_foo()", the graph will be saved in the foo format.

Command line parameters are as follows:

    $ ./parse_netjson.py 
    usage: parse_netjson.py [-h] -i INPUTFILE -t {edgelist,graphml,gpickle}
                        [-o OUTPUTFILE]


'-i' and '-t' are required, if you don't use '-o' a new file named like the input one will be generated with the type as extension.



