#!/usr/bin/python2.4
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2005/06/09 00:00:38 $
#   $RCSfile: demo5.py,v $
#   $Revision: 1.18 $
#
#   $Id: demo5.py,v 1.18 2005/06/09 00:00:38 brpreiss Exp $
#

"""
Provides the Demo5 class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2005/06/09 00:00:38 $"
__version__ = "$Revision: 1.18 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

import sys
from opus7.generalTree import GeneralTree
from opus7.binaryTree import BinaryTree
from opus7.naryTree import NaryTree
from opus7.binarySearchTree import BinarySearchTree
from opus7.avlTree import AVLTree
from opus7.mWayTree import MWayTree
from opus7.bTree import BTree

class Demo5(object):

    @staticmethod
    def main(*argv):
        "Demostration program number 5."
        print Demo5.main.__doc__
        GeneralTree.main(*argv)
        BinaryTree.main(*argv)
        NaryTree.main(*argv)
        BinarySearchTree.main(*argv)
        AVLTree.main(*argv)
        MWayTree.main(*argv)
        BTree.main(*argv)
        return 0

if __name__ == "__main__":
    sys.exit(Demo5.main(*sys.argv))
