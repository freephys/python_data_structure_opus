#!/usr/bin/python2.4
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2005/06/09 00:00:38 $
#   $RCSfile: demo10.py,v $
#   $Revision: 1.15 $
#
#   $Id: demo10.py,v 1.15 2005/06/09 00:00:38 brpreiss Exp $
#

"""
Provides the Demo10 class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2005/06/09 00:00:38 $"
__version__ = "$Revision: 1.15 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

import sys
from opus7.graphAsMatrix import GraphAsMatrix
from opus7.digraphAsMatrix import DigraphAsMatrix
from opus7.graphAsLists import GraphAsLists
from opus7.digraphAsLists import DigraphAsLists

class Demo10(object):

    @staticmethod
    def main(*argv):
        "Demostration program number 10."
        print Demo10.main.__doc__
        GraphAsMatrix.main(*argv)
        DigraphAsMatrix.main(*argv)
        GraphAsLists.main(*argv)
        DigraphAsLists.main(*argv)
        return 0

if __name__ == "__main__":
    sys.exit(Demo10.main(*sys.argv))
