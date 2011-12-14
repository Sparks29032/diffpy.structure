#!/usr/bin/env python
##############################################################################
#
# diffpy.Structure  by DANSE Diffraction group
#                   Simon J. L. Billinge
#                   (c) 2010 Trustees of the Columbia University
#                   in the City of New York.  All rights reserved.
#
# File coded by:    Pavol Juhas
#
# See AUTHORS.txt for a list of people who contributed.
# See LICENSE.txt for license information.
#
##############################################################################

"""Unit tests for diffpy.Structure.
"""

# version
__id__ = '$Id$'

def test():
    '''Execute all unit tests for the diffpy.Structure package.
    Return a unittest TestResult object.
    '''
    import unittest
    modulenames = '''
        diffpy.Structure.tests.TestLattice
        diffpy.Structure.tests.TestP_cif
        diffpy.Structure.tests.TestP_discus
        diffpy.Structure.tests.TestP_pdffit
        diffpy.Structure.tests.TestParsers
        diffpy.Structure.tests.TestStructure
        diffpy.Structure.tests.TestSuperCell
        diffpy.Structure.tests.TestSymmetryUtilities
    '''.split()
    suite = unittest.TestSuite()
    loader = unittest.defaultTestLoader
    for mname in modulenames:
        exec ('import %s as mobj' % mname)
        suite.addTests(loader.loadTestsFromModule(mobj))
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    return result

# End of file