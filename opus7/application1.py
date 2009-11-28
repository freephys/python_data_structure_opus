#!/usr/bin/python2.4
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2005/06/09 00:00:37 $
#   $RCSfile: application1.py,v $
#   $Revision: 1.9 $
#
#   $Id: application1.py,v 1.9 2005/06/09 00:00:37 brpreiss Exp $
#

"""
Provides the Application1 class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2005/06/09 00:00:37 $"
__version__ = "$Revision: 1.9 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

import sys
from opus7.algorithms import Algorithms

class Application1(object):

    @staticmethod
    def main(*argv):
        "Application program number 1. (calculator)"
        print Application1.main.__doc__
        Algorithms.calculator(sys.stdin, sys.stdout)
        return 0

if __name__ == "__main__":
    sys.exit(Application1.main(*sys.argv))
