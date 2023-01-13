from Course_13.class_for_testing import Operation
import unittest

class TestOperation(unittest.TestCase):
    def add_test(self):
        self.assertEqual(3, Operation.add(1,2))

    def test_sub(self):
        self.assertEqual(-1, Operation.sub(1, 2))


if __name__ == '__main__':
    unittest.main()

# def add_test():
#     i = 1, 2
#     o = 3
#     assert o == Operation.add(i[0], i[1])
#
# def sub_test():
#     i = 1, 2
#     o = -1
#     assert o == Operation.sub(i[0], i[1])
#
#
# def main():
#     add_test()
# main()