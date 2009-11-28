#!/usr/bin/python2.4
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2005/06/09 00:00:38 $
#   $RCSfile: demo9.py,v $
#   $Revision: 1.10 $
#
#   $Id: demo9.py,v 1.10 2005/06/09 00:00:38 brpreiss Exp $
#

"""
Provides the Demo9 class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2005/06/09 00:00:38 $"
__version__ = "$Revision: 1.10 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

import sys
from opus7.sorter import Sorter
from opus7.straightInsertionSorter import StraightInsertionSorter
from opus7.binaryInsertionSorter import BinaryInsertionSorter
from opus7.bubbleSorter import BubbleSorter
from opus7.straightSelectionSorter import StraightSelectionSorter
from opus7.medianOfThreeQuickSorter import MedianOfThreeQuickSorter
from opus7.heapSorter import HeapSorter
from opus7.twoWayMergeSorter import TwoWayMergeSorter
from opus7.bucketSorter import BucketSorter
from opus7.radixSorter import RadixSorter

class Demo9(object):

    @staticmethod
    def main(*argv):
        "Demonstration program number 9."
        #print Demo9.main.__doc__
        if len(argv) != 4:
            print "usage: %s size seed mask" % (argv[0])
            sys.exit(1)
        n = int(argv[1])
        seed = int(argv[2])
        mask = int(argv[3])
        if (mask & 04) != 0:
            Sorter.test(StraightInsertionSorter(), n, seed)
            Sorter.test(BinaryInsertionSorter(), n, seed)
            Sorter.test(BubbleSorter(), n, seed)
            Sorter.test(StraightSelectionSorter(), n, seed)
        if (mask & 02) != 0:
            Sorter.test(MedianOfThreeQuickSorter(), n, seed)
            Sorter.test(HeapSorter(), n, seed)
            Sorter.test(TwoWayMergeSorter(), n, seed)
        if (mask & 01) != 0:
            Sorter.test(BucketSorter(1024), n, seed, 1024)
            Sorter.test(RadixSorter(), n, seed)
        return 0

if __name__ == "__main__":
    sys.exit(Demo9.main(*sys.argv))
