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
        self.assertIsInstance(Calc.sum(2, 3.0), float)

    def test_Add_Computing(self):
        print('test_Add_Computing')
        self.assertEqual(Calc.sum(0.0, 0), 0)
        self.assertEqual(Calc.sum(3, 3), 6.0)
        self.assertEqual(Calc.sum(-5, 2), -3)
        self.assertEqual(Calc.sum(105, 5.0), 110)

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
        self.assertIsInstance(Calc.minus(2, 3.0), float)

    def test_Subtract_Computing(self):
        print('test_Subtract_Computing')
        self.assertEqual(Calc.minus(0.0, 0), 0)
        self.assertEqual(Calc.minus(-5, -5), 0.0)
        self.assertEqual(Calc.minus(-5, 2), -7)
        self.assertEqual(Calc.minus(10, 5.0), 5)

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
        self.assertIsInstance(Calc.mul(2, 3.0), float)

    def test_Multiply_Computing(self):
        print('test_Multiply_Computing')
        self.assertEqual(Calc.mul(0.0, 0), 0)
        self.assertEqual(Calc.mul(100, 2), 200.0)
        self.assertEqual(Calc.mul(-5, 2), -10)
        self.assertEqual(Calc.mul(10, 5.0), 50)

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
        self.assertIsInstance(Calc.div(50, 2.0), float)

    def test_Divide_Computing(self):
        print('test_Divide_Computing')
        self.assertEqual(Calc.mul(0.0, 1), 0)
        self.assertEqual(Calc.div(100, 2.0), 50)
        self.assertEqual(Calc.div(-50, 2), -25)
        self.assertEqual(Calc.div(-5, -5), 1.0)

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


class TestPow(unittest.TestCase):
    """
    Testing rise any number to the power in calculator
    """
    def setUp(self) -> None:
        print('setUp')

    def test_Power_DataInputs(self):
        print('test_Power_DataInputs')
        self.assertIsInstance(Calc.pow(4, 2), int)
        self.assertIsInstance(Calc.pow(2.0, 2), float)
        self.assertIsInstance(Calc.pow(50, 2.0), float)

    def test_Power_Computing(self):
        print('test_Power_Computing')
        self.assertEqual(Calc.pow(0.0, 0), 1)
        self.assertEqual(Calc.pow(0, 1), 0.0)
        self.assertEqual(Calc.pow(-5, 11), -48828125)
        self.assertEqual(Calc.pow(-5.0, 2), 25)

    def test_Power_RaiseExceptions(self):
        print('test_Power_RaiseExceptions')
        # self.assertRaises(TypeError, Calc.pow, "10", 2)
        with self.assertRaises(TypeError):
            Calc.pow("10", 2)

    def tearDown(self) -> None:
        print('tearDown\n')


class TestPerc(unittest.TestCase):
    """
    Testing percentage of any number in calculator
    """
    def setUp(self) -> None:
        print('setUp')

    def test_Percentage_DataInputs(self):
        print('test_Percentage_DataInputs')
        self.assertIsInstance(Calc.perc(1, 2), float)
        self.assertIsInstance(Calc.perc(2.0, 2), float)
        self.assertIsInstance(Calc.perc(2, 3.0), float)

    def test_Percentage_Computing(self):
        print('test_Percentage_Computing')
        self.assertEqual(Calc.perc(0.0, 0), 0)
        self.assertEqual(Calc.perc(35, 500), 175.0)
        self.assertEqual(Calc.perc(10, 100.0), 10)

    def test_Percentage_SpecialCase(self):
        print('test_Percentage_RaiseExceptions')
        with self.assertRaises(TypeError):
            Calc.perc("10", 100)

    def tearDown(self) -> None:
        print('tearDown\n')


class TestRoot(unittest.TestCase):
    """
    Testing square root of any number in calculator
    """
    def setUp(self) -> None:
        print('setUp')

    def test_Sqrt_DataInputs(self):
        print('test_Sqrt_DataInputs')
        self.assertIsInstance(Calc.root(4), float)
        self.assertIsInstance(Calc.root(9.0), float)

    def test_Sqrt_Computing(self):
        print('test_Sqrt_Computing')
        self.assertEqual(Calc.root(0.0), 0)
        self.assertEqual(Calc.root(625), 25.0)
        self.assertEqual(Calc.root(4.0), 2.0)

    def test_Division_RaiseExceptions(self):
        print('test_Sqrt_RaiseExceptions')
        # self.assertRaises(ValueError, Calc.root, -25)
        with self.assertRaises(ValueError):
            Calc.root(-25)
        # self.assertRaises(TypeError, Calc.root, "4")
        with self.assertRaises(TypeError):
            Calc.root("25")

    def tearDown(self) -> None:
        print('tearDown\n')


if __name__ == '__main__':
    unittest.main()
