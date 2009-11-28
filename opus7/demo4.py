#!/usr/bin/python2.4
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2005/06/09 00:00:38 $
#   $RCSfile: demo4.py,v $
#   $Revision: 1.17 $
#
#   $Id: demo4.py,v 1.17 2005/06/09 00:00:38 brpreiss Exp $
#

"""
Provides the Demo4 class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2005/06/09 00:00:38 $"
__version__ = "$Revision: 1.17 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

import sys
from opus7.strng import String
from opus7.chainedHashTable import ChainedHashTable
from opus7.chainedScatterTable import ChainedScatterTable
from opus7.openScatterTable import OpenScatterTable
from opus7.openScatterTableV2 import OpenScatterTableV2

class Demo4(object):

    @staticmethod
    def main(*argv):
        "Demostration program number 4."
        print Demo4.main.__doc__
        String.testHash()
        ChainedHashTable.main(*argv)
        ChainedScatterTable.main(*argv)
        OpenScatterTable.main(*argv)
        OpenScatterTableV2.main(*argv)
        return 0

if __name__ == "__main__":
    sys.exit(Demo4.main(*sys.argv))
