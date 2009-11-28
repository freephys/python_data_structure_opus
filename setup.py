#!/usr/bin/python2
#
#   Copyright (c) 2003 by Bruno R. Preiss, P.Eng.
#
#   $Author: brpreiss $
#   $Date: 2003/09/07 13:52:21 $
#   $RCSfile: setup.py,v $
#   $Revision: 1.3 $
#
#   $Id: setup.py,v 1.3 2003/09/07 13:52:21 brpreiss Exp $
#

"""
Distutils setup file for the Opus7 package.
"""

__author__  = "Bruno R. Preiss, P.Eng."
__date__    = "$Date: 2003/09/07 13:52:21 $"
__version__ = "$Revision: 1.3 $"
__credits__ = "Copyright (c) 2003 by Bruno R. Preiss, P.Eng."

from distutils.core import setup

setup(
    name="Opus7",
    version="1.0",
    description="Opus7",
    author="Bruno R. Preiss",
    author_email="brpreiss@brpreiss.com",
    url="http://www.brpreiss.com/books/opus7",
    packages=["opus7"],
    data_files=[("opus7",["opus7/dict.txt"])],
)
