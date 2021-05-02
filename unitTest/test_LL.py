#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
from alg.LinkedList import *

def test_LL_None():
    llist = LinkedList()
    print(llist)
    assert llist == []

def test_LL():
    head = Node("a")
    llist = LinkedList()
    llist.head = head
    assert llist == "1 -> None"


