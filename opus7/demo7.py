#!/usr/bin/python2.4
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2005/06/09 00:00:38 $
#   $RCSfile: demo7.py,v $
#   $Revision: 1.13 $
#
#   $Id: demo7.py,v 1.13 2005/06/09 00:00:38 brpreiss Exp $
#

"""
Provides the Demo7 class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2005/06/09 00:00:38 $"
__version__ = "$Revision: 1.13 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

import sys
from opus7.setAsArray import SetAsArray
from opus7.setAsBitVector import SetAsBitVector
from opus7.multisetAsArray import MultisetAsArray
from opus7.multisetAsLinkedList import MultisetAsLinkedList
from opus7.partitionAsForest import PartitionAsForest
from opus7.partitionAsForestV2 import PartitionAsForestV2
from opus7.partitionAsForestV3 import PartitionAsForestV3

class Demo7(object):

    @staticmethod
    def main(*argv):
        "Demostration program number 7."
        print Demo7.main.__doc__
        SetAsArray.main(*argv)
        SetAsBitVector.main(*argv)
        MultisetAsArray.main(*argv)
        MultisetAsLinkedList.main(*argv)
        PartitionAsForest.main(*argv)
        PartitionAsForestV2.main(*argv)
        PartitionAsForestV3.main(*argv)
        return 0

if __name__ == "__main__":
    sys.exit(Demo7.main(*sys.argv))
