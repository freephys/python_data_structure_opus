#!/usr/bin/python2.4
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2005/06/09 00:00:37 $
#   $RCSfile: application8.py,v $
#   $Revision: 1.8 $
#
#   $Id: application8.py,v 1.8 2005/06/09 00:00:37 brpreiss Exp $
#

"""
Provides the Application8 class.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2005/06/09 00:00:37 $"
__version__ = "$Revision: 1.8 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

import sys
from opus7.simulation import Simulation

class Application8(object):

    @staticmethod
    def main(*argv):
        "Application program number 8."
        print Application8.main.__doc__
        simulation = Simulation()
        simulation.run(10000)
        return 0

if __name__ == "__main__":
    sys.exit(Application8.main(*sys.argv))
