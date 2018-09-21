
"""
 * Excerpted from "The Definitive ANTLR 4 Reference",
 * published by The Pragmatic Bookshelf.
 * Copyrights apply to this code. It may not be used to create training material, 
 * courses, books, articles, and the like. Contact us if you are in doubt.
 * We make no guarantees that this code is fit for any purpose. 
 * Visit http://www.pragmaticprogrammer.com/titles/tpantlr2 for more book information.

 Translated to Python by Peter C Marks

"""


# CODE TAKEN FROM : https://github.com/pcmarks/Jython-ANTLR4-Book-Examples/blob/master/src/listeners/CallGraph.py
# The code generates a graph and dot file from the graph (Few modifications made)

import sys
import pydot
import subprocess
from antlr4 import *
from myGrammarLexer import myGrammarLexer
from myGrammarParser import myGrammarParser
from myGrammarListener import myGrammarListener
from antlr4.tree.Trees import Trees
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from subprocess import check_call

class Graph():

    def __init__(self):
        self.nodes = []
        self.edges = {}

    def edge(self, source, target):
        self.edges.map(source, target)

    def toString(self):
        return "edges: %s, functions: %s" % (self.edges.toString(), self.nodes)

    def toDOT(self):
        f = open("test.dot","w")
        buf = ''.join(["digraph G{\n", "  ranksep=.25;\n", "  edge [arrowsize=.5]\n",
                        "  node [shape=circle, fontname=\"ArialNarrow\",\n",
                        "        fontsize=12, fixedsize=true, height=.45];\n", "  "])

        for key, values in self.edges.iteritems():
            for value in values:
                buf = ''.join([buf, "  ", key, " -> ", value, ";\n"])
        buf = buf + "}\n"

        f.write(buf)
        f.close()
        return buf

class FunctionListener(myGrammarListener):

    def __init__(self):
        self.graph = Graph()
        self.currentFunctionName = None

    def enterFunctionDecl(self, ctx):
        self.currentFunctionName = ctx.ID().getText()
        self.graph.nodes.append(self.currentFunctionName)

    def exitCall(self, ctx):
        funcName = ctx.ID().getText()
        self.graph.edge(self.currentFunctionName, funcName)

def main():
    ais = FileStream(sys.argv[1])
    lexer = myGrammarLexer(ais)
    tokens = CommonTokenStream(lexer)
    parser = myGrammarParser(tokens)
    tree = parser.rules()

    print Trees.toStringTree(tree,None,parser)

    # generating dot file
    walker = ParseTreeWalker()
    collector = FunctionListener()
    walker.walk(collector, tree)
    print collector.graph.toDOT()


    # using graphviz
    subprocess.check_call(["dot", "-Tpng", "test.dot", "-o", "dt.png"])

if __name__ == '__main__':
    main()




# TERMINAL COMMAND example
# python testing.py input.txt