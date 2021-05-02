#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
from alg.LinkedList import *

def test_LL_None():
    llist = LinkedList()
    print(llist)
    assert str(llist) == "[]"

def test_LL():
    llist = LinkedList([1,2,3])
    assert str(llist) == "[1, 2, 3]"


