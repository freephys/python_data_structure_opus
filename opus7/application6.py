#!/usr/bin/python2.4
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2005/06/09 00:00:37 $
#   $RCSfile: application6.py,v $
#   $Revision: 1.8 $
#
#   $Id: application6.py,v 1.8 2005/06/09 00:00:37 brpreiss Exp $
#

"""
Provides the Application6 class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2005/06/09 00:00:37 $"
__version__ = "$Revision: 1.8 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

import sys
from opus7.expressionTree import ExpressionTree

class Application6(object):

    @staticmethod
    def main(*argv):
        "Application program number 6. (expression tree)"
        print Application6.main.__doc__
        expression = ExpressionTree.parsePostfix(sys.stdin)
        sys.stdout.write(str(expression) + "\n")
        return 0

if __name__ == "__main__":
    sys.exit(Application6.main(*sys.argv))
