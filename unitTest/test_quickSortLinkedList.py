import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../alg'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

import unittest
from alg import quickSortLinkedList

# unit test file