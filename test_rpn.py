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

    def test_exp(self):
        result = rpn.calculate('2 3 ^')
        self.assertEqual(8, result)

    def test_exp2(self):
        result = rpn.calculate('123 0 ^')
        self.assertEqual(1, result)

    def test_toomany(self):
        with self.assertRaises(TypeError):
            result = rpn.calculate('1 1 1 +')

    def test_sin(self):
        result = rpn.calculate('0 sin')
        self.assertEqual(0, result)

    def test_sin2(self):
        result = rpn.calculate('90 sin')
        self.assertEqual(1, result)


    def test_cos(self):
        result = rpn.calculate('0 cos')
        self.assertEqual(1, result)

    def test_cos2(self):
        result = rpn.calculate('90 cos')
        self.assertEqual(0, result)

    def test_cos180(self):
        result = rpn.calculate('180 cos')
        self.assertEqual(-1, result)

    def test_tan(self):
        result = rpn.calculate('0 tan')
        self.assertEqual(0, result)

    def test_tan2(self):
        result = rpn.calculate('45 tan')
        self.assertEqual(1, result)

    def test_sin180(self):
        result = rpn.calculate('180 sin')
        self.assertEqual(0, result)
