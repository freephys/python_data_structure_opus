#!/usr/bin/python2.4
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2005/06/09 00:00:37 $
#   $RCSfile: application12.py,v $
#   $Revision: 1.10 $
#
#   $Id: application12.py,v 1.10 2005/06/09 00:00:37 brpreiss Exp $
#

"""
Provides the Applicstion12 class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2005/06/09 00:00:37 $"
__version__ = "$Revision: 1.10 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

import sys
from opus7.array import Array
from opus7.depthFirstSolver import DepthFirstSolver
from opus7.depthFirstBranchAndBoundSolver import DepthFirstBranchAndBoundSolver
from opus7.breadthFirstSolver import BreadthFirstSolver
from opus7.breadthFirstBranchAndBoundSolver import BreadthFirstBranchAndBoundSolver
from opus7.scalesBalancingProblem import ScalesBalancingProblem
from opus7.zeroOneKnapsackProblem import ZeroOneKnapsackProblem

class Application12(object):

    @staticmethod
    def main(*argv):
        "Application12 test program."
        print Application12.main.__doc__
        solver1 = DepthFirstSolver()
        solver2 = DepthFirstBranchAndBoundSolver()
        solver3 = BreadthFirstSolver()
        solver4 = BreadthFirstBranchAndBoundSolver()

        weights = Array(5)
        weights[0] = 20
        weights[1] = 20
        weights[2] = 2
        weights[3] = 2
        weights[4] = 1
        scales = ScalesBalancingProblem(weights)
        print scales.solve(solver1)
        print scales.solve(solver2)
        print scales.solve(solver3)
        print scales.solve(solver4)


        weights = Array(6)
        weights[0] = 100
        weights[1] = 50
        weights[2] = 45
        weights[3] = 20
        weights[4] = 10
        weights[5] = 5
        profits = Array(6)
        profits[0] = 40
        profits[1] = 35
        profits[2] = 18
        profits[3] = 4
        profits[4] = 10
        profits[5] = 2
        knapsack = ZeroOneKnapsackProblem(weights, profits, 100)
        print knapsack.solve(solver1)
        print knapsack.solve(solver2)
        print knapsack.solve(solver3)
        print knapsack.solve(solver4)
        return 0

if __name__ == "__main__":
    sys.exit(Application12.main(*sys.argv))
