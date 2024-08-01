import unittest
from draw import fib 

class TestFibonacci(unittest.TestCase):

    # def setUp(self):
    #     self.dp_list = [0] * 201 

    def test_base_fib(self):
        self.dp_list = [0] * 3
        self.assertEqual(fib(1, self.dp_list), 1)
        print("fib 1 = " + str(fib(1, self.dp_list)))
        self.assertEqual(fib(2, self.dp_list), 1)
        print("fib 2 = " + str(fib(2, self.dp_list)))

    def test_fib(self):
        self.dp_list = [0] * 16
        self.assertEqual(fib(3, self.dp_list), 2)
        print("fib 3 = " + str(fib(3, self.dp_list)))
        self.assertEqual(fib(4, self.dp_list), 3)
        print("fib 4 = " + str(fib(4, self.dp_list)))
        self.assertEqual(fib(5, self.dp_list), 5)
        print("fib 5 = " + str(fib(5, self.dp_list)))
        self.assertEqual(fib(10, self.dp_list), 55)
        print("fib 10 = " + str(fib(10, self.dp_list)))
        self.assertEqual(fib(15, self.dp_list), 610)
        print("fib 15 = " + str(fib(15, self.dp_list)))

    def test_large_fib(self):
        self.dp_list = [0] * 41
        self.assertEqual(fib(20, self.dp_list), 6765)
        self.assertEqual(fib(30, self.dp_list), 832040)
        self.assertEqual(fib(40, self.dp_list), 102334155)

if __name__ == '__main__':
    unittest.main()

