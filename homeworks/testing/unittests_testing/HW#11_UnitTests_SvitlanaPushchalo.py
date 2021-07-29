import unittest
from calc import Calc


class TestSum(unittest.TestCase):
    """
    Testing adding of values in calculator
    """

    def setUp(self) -> None:
        print('setUp')

    def test_Add_DataInputs(self):
        print('test_Add_DataInputs')
        self.assertIsInstance(Calc.sum(1, 2), int)
        self.assertIsInstance(Calc.sum(2.0, 2), float)
        self.assertIsInstance(Calc.sum(2.0, 3.0), float)
        self.assertIsInstance(Calc.sum(2, 3.0), float)

    def test_Add_Computing(self):
        print('test_Add_Computing')
        self.assertEqual(Calc.sum(3, 3), 6)
        self.assertEqual(Calc.sum(0, 0), 0)
        self.assertEqual(Calc.sum(-5, 2), -3)
        self.assertEqual(Calc.sum(105.0, 5), 110)
        self.assertEqual(Calc.sum(10, 5.0), 15.0)

    def test_Add_RaiseExceptions(self):
        print('test_Add_RaiseExceptions')
        # self.assertRaises(TypeError, Calc.sum, "1", 2)
        with self.assertRaises(TypeError):
            Calc.sum("1", 2)

    def tearDown(self) -> None:
        print('tearDown\n')


class TestMinus(unittest.TestCase):
    """
    Testing subtraction of values in calculator
    """
    def setUp(self) -> None:
        print('setUp')

    def test_Subtract_DataInputs(self):
        print('test_Subtract_DataInputs')
        self.assertIsInstance(Calc.minus(1, 2), int)
        self.assertIsInstance(Calc.minus(2.0, 2), float)
        self.assertIsInstance(Calc.minus(2.0, 3.0), float)
        self.assertIsInstance(Calc.minus(2, 3.0), float)

    def test_Subtract_Computing(self):
        print('test_Subtract_Computing')
        self.assertEqual(Calc.minus(100, 2), 98)
        self.assertEqual(Calc.minus(0, 0), 0)
        self.assertEqual(Calc.minus(-5, 2), -7)
        self.assertEqual(Calc.minus(-5, -5), 0)
        self.assertEqual(Calc.minus(105.0, 5), 100)
        self.assertEqual(Calc.minus(10, 5.0), 5.0)

    def test_Subtract_RaiseExceptions(self):
        print('test_Subtract_RaiseExceptions')
        # self.assertRaises(TypeError, Calc.minus, 52, "2")
        with self.assertRaises(TypeError):
            Calc.minus(52, "2")

    def tearDown(self) -> None:
        print('tearDown\n')


class TestMult(unittest.TestCase):
    """
    Testing multiplication of values in calculator
    """
    def setUp(self) -> None:
        print('setUp')

    def test_Multiply_DataInputs(self):
        print('test_Multiply_DataInputs')
        self.assertIsInstance(Calc.mul(1, 2), int)
        self.assertIsInstance(Calc.mul(2.0, 2), float)
        self.assertIsInstance(Calc.mul(2.0, 3.0), float)
        self.assertIsInstance(Calc.mul(2, 3.0), float)

    def test_Multiply_Computing(self):
        print('test_Multiply_Computing')
        self.assertEqual(Calc.mul(100, 2), 200)
        self.assertEqual(Calc.mul(0, 0), 0)
        self.assertEqual(Calc.mul(-5, 2), -10)
        self.assertEqual(Calc.mul(10.0, 5), 50)
        self.assertEqual(Calc.mul(10, 5.0), 50.0)

    def test_Multiply_SpecialCase(self):
        print('test_Multiply_SpecialCase')
        self.assertEqual(Calc.mul(3, '500'), '500500500')

    def tearDown(self) -> None:
        print('tearDown\n')


class TestDiv(unittest.TestCase):
    """
    Testing division of values in calculator
    """
    def setUp(self) -> None:
        print('setUp')

    def test_Divide_DataInputs(self):
        print('test_Divide_DataInputs')
        self.assertIsInstance(Calc.div(4, 2), float)
        self.assertIsInstance(Calc.div(2.0, 2), float)
        self.assertIsInstance(Calc.div(50.0, 2.0), float)
        self.assertIsInstance(Calc.div(50, 2.0), float)

    def test_Divide_Computing(self):
        print('test_Divide_Computing')
        self.assertEqual(Calc.div(100, 2.0), 50)
        self.assertEqual(Calc.div(-50, 2), -25)
        self.assertEqual(Calc.div(-5, -5), 1)


    def test_Division_RaiseExceptions(self):
        print('test_Division_RaiseExceptions')
        # self.assertRaises(ZeroDivisionError, Calc.div, 10, 0)
        with self.assertRaises(ZeroDivisionError):
            Calc.div(10, 0)
        # self.assertRaises(TypeError, Calc.div, 52, "2")
        with self.assertRaises(TypeError):
            Calc.div(52, "2")

    def tearDown(self) -> None:
        print('tearDown\n')


