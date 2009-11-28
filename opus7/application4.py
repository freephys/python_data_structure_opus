#!/usr/bin/python2.4
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2005/06/09 00:00:37 $
#   $RCSfile: application4.py,v $
#   $Revision: 1.8 $
#
#   $Id: application4.py,v 1.8 2005/06/09 00:00:37 brpreiss Exp $
#

"""
Provides the Application4 class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2005/06/09 00:00:37 $"
__version__ = "$Revision: 1.8 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

import sys
from opus7.polynomial import Polynomial
from opus7.polynomialAsSortedList import PolynomialAsSortedList

class Application4(object):

    @staticmethod
    def main(*argv):
        "Application program number 4."
        print Application4.main.__doc__
        p1 = PolynomialAsSortedList()
        p1.addTerm(Polynomial.Term(4.5, 5))
        p1.addTerm(Polynomial.Term(3.2, 14))
        print p1

        p2 = PolynomialAsSortedList()
        p2.addTerm(Polynomial.Term(7.8, 3))
        p2.addTerm(Polynomial.Term(1.6, 14))
        p2.addTerm(Polynomial.Term(9.999, 27))
        print p2

        p3 = p1 + p2
        print p3
        return 0

if __name__ == "__main__":
    sys.exit(Application4.main(*sys.argv))
