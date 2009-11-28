#!/usr/bin/python2.4
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2005/06/09 00:00:38 $
#   $RCSfile: demo3.py,v $
#   $Revision: 1.16 $
#
#   $Id: demo3.py,v 1.16 2005/06/09 00:00:38 brpreiss Exp $
#

"""
Provides the Demo3 class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2005/06/09 00:00:38 $"
__version__ = "$Revision: 1.16 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

import sys
from opus7.orderedListAsArray import OrderedListAsArray
from opus7.orderedListAsLinkedList import OrderedListAsLinkedList
from opus7.sortedListAsArray import SortedListAsArray
from opus7.sortedListAsLinkedList import SortedListAsLinkedList

class Demo3(object):

    @staticmethod
    def main(*argv):
        "Demostration program number 3."
        print Demo3.main.__doc__
        OrderedListAsArray.main(*argv)
        OrderedListAsLinkedList.main(*argv)
        SortedListAsArray.main(*argv)
        SortedListAsLinkedList.main(*argv)
        return 0

if __name__ == "__main__":
    sys.exit(Demo3.main(*sys.argv))
