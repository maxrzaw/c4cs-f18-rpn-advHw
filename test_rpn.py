import unittest
import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate('1 1 +')
        self.assertEqual(2, result)

    def test_add2(self):
        result = rpn.calculate('1 3 +')
        self.assertEqual(4, result)

    def test_sub(self):
        result = rpn.calculate('3 1 -')
        self.assertEqual(2, result)
        
    def test_sub2(self):
        result = rpn.calculate('1 3 -')
        self.assertEqual(-2, result)

    def test_mul(self):
        result = rpn.calculate('1 1 *')
        self.assertEqual(1, result)

    def test_mul2(self):
        result = rpn.calculate('1 3 *')
        self.assertEqual(3, result)

    def test_div(self):
        result = rpn.calculate('6 3 /')
        self.assertEqual(2, result)
        
    def test_div2(self):
        result = rpn.calculate('3 3 /')
        self.assertEqual(1, result)
    def test_chain(self):
        result = rpn.calculate('1 2 + 1 +')
        self.assertEqual(4, result)

