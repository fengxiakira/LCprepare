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

def test_addFirst():
    llist = LinkedList([1, 2, 3])
    llist.add_first(Node(5))
    assert str(llist) == "[5, 1, 2, 3]"

def test_insertAfter():
    llist = LinkedList([1, 1, 2, 2, 3])
    llist.insert_after(2,Node(8))
    assert str(llist) == ""

def test_insertBefor():
    llist = LinkedList([1, 1, 2, 2, 3])
    llist.insert_before(2,Node(6))
    # assert str(llist) == ""
    # llist1 = LinkedList()
    llist.insert_before(7, Node(6))
    assert str(llist) == ""

def test_remove():
    llist = LinkedList([1, 1, 2, 4, 3])
    llist.remove_node(3)
    assert str(llist) == "[1, 1, 2, 4]"




