#!/usr/bin/python2.4
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2005/06/09 00:00:37 $
#   $RCSfile: application11.py,v $
#   $Revision: 1.10 $
#
#   $Id: application11.py,v 1.10 2005/06/09 00:00:37 brpreiss Exp $
#

"""
Provides the Application11 class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2005/06/09 00:00:37 $"
__version__ = "$Revision: 1.10 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

import sys
from opus7.graphAsMatrix import GraphAsMatrix
from opus7.graphAsLists import GraphAsLists
from opus7.digraphAsMatrix import DigraphAsMatrix
from opus7.digraphAsLists import DigraphAsLists
from opus7.algorithms import Algorithms

class Application11(object):

    @staticmethod
    def weightedGraphTest(g):
        "Weighted graph test program."
        print Application11.weightedGraphTest.__doc__
        g.addVertex(0, 123)
        g.addVertex(1, 234)
        g.addVertex(2, 345)
        g.addEdge(0, 1, 3)
        g.addEdge(0, 2, 1)
        g.addEdge(1, 2, 4)
        print "Prim's Algorithm"
        g2 = Algorithms.PrimsAlgorithm(g, 0)
        print g2
        print "Kruskal's Algorithm"
        g2 = Algorithms.KruskalsAlgorithm(g)
        print g2

    @staticmethod
    def weightedDigraphTest(g):
        "Weighted digraph test program."
        print Application11.weightedDigraphTest.__doc__
        Application11.weightedGraphTest(g)
        print "Dijkstra's Algorithm"
        g2 = Algorithms.DijkstrasAlgorithm(g, 0)
        print g2
        print "Floyd's Algorithm"
        g2 = Algorithms.FloydsAlgorithm(g)
        print g2

    @staticmethod
    def main(*argv):
        "Application11 test program."
        print Application11.main.__doc__

        g = GraphAsMatrix(32)
        Application11.weightedGraphTest(g)

        g = GraphAsLists(32)
        Application11.weightedGraphTest(g)

        g = DigraphAsMatrix(32)
        Application11.weightedDigraphTest(g)

        g = DigraphAsLists(32)
        Application11.weightedDigraphTest(g)

        print "Critical path analysis."
        g = DigraphAsMatrix(10)
        for v in xrange(10):
            g.addVertex(v)
        g.addEdge(0, 1, 3)
        g.addEdge(1, 2, 1)
        g.addEdge(1, 3, 4)
        g.addEdge(2, 4, 0)
        g.addEdge(3, 4, 0)
        g.addEdge(4, 5, 1)
        g.addEdge(5, 6, 9)
        g.addEdge(5, 7, 5)
        g.addEdge(6, 8, 0)
        g.addEdge(7, 8, 0)
        g.addEdge(8, 9, 2)
        print g
        g = Algorithms.criticalPathAnalysis(g)
        print g
        return 0

if __name__ == "__main__":
    sys.exit(Application11.main(*sys.argv))
