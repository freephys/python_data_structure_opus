#!/usr/bin/python2.4
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2005/06/09 00:00:37 $
#   $RCSfile: application5.py,v $
#   $Revision: 1.8 $
#
#   $Id: application5.py,v 1.8 2005/06/09 00:00:37 brpreiss Exp $
#

"""
Provides the Application5 class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2005/06/09 00:00:37 $"
__version__ = "$Revision: 1.8 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

import sys
from opus7.algorithms import Algorithms

class Application5(object):

    @staticmethod
    def main(*argv):
        "Application program number 5. (word counter)"
        print Application5.main.__doc__
        Algorithms.wordCounter(sys.stdin, sys.stdout)
        return 0

if __name__ == "__main__":
    sys.exit(Application5.main(*sys.argv))
