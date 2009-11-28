#!/usr/bin/python2.4
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2005/06/09 00:00:38 $
#   $RCSfile: demo1.py,v $
#   $Revision: 1.10 $
#
#   $Id: demo1.py,v 1.10 2005/06/09 00:00:38 brpreiss Exp $
#

"""
Provides the Demo1 class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2005/06/09 00:00:38 $"
__version__ = "$Revision: 1.10 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

import sys
from opus7.denseMatrix import DenseMatrix
from opus7.sparseMatrixAsArray import SparseMatrixAsArray
from opus7.sparseMatrixAsVector import SparseMatrixAsVector
from opus7.sparseMatrixAsLinkedList import SparseMatrixAsLinkedList

class Demo1(object):

    @staticmethod
    def main(*argv):
        "Demostration program number 1."
        print Demo1.main.__doc__
        DenseMatrix.main(*argv)
        SparseMatrixAsArray.main(*argv)
        SparseMatrixAsVector.main(*argv)
        SparseMatrixAsLinkedList.main(*argv)
        return 0

if __name__ == "__main__":
    sys.exit(Demo1.main(*sys.argv))
