# python -m pytest -v --cov

import stack
import unittest


class TestStack(unittest.TestCase): 
    def test_type_stack(self):
        s = stack.Stack()
        assert str(type(s)) == "<class 'stack.Stack'>"

    def test_constructor(self):
        s = stack.Stack()
        assert len(s) == 0

    def test_push(self):
        pu = stack.Stack()
        pu.push(3)
        assert len(pu) == 1
        pu.push(5)
        assert len(pu) == 2

    def test_pop(self):
        po = stack.Stack()
        po.push("hello")
        po.push("world")
        assert po.pop() == "world"
        assert po.pop() == "hello"
        assert po.pop() is None
