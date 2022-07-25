import unittest
from contrived_func import contrived_func


class TestContrivedFunction(unittest.TestCase):

    # test1 leads to:
    #  branch 0 executing
    #  condition 0 being actually evaluated and evaluating to True
    #  condition 1 being actually evaluated and evaluating to True
    #  contrived_function returning True
    def test1(self):
        self.assertTrue(contrived_func(125))

    # test2 leads to:
    #  branch 1 executing
    #  condition 0 being actually evaluated and evaluating to True
    #  condition 1 being actually evaluated and evaluating to False
    #  condition 2 being actually evaluated and evaluating to True
    #  condition 3 being actually evaluated and evaluating to True
    #  condition 4 being actually evaluated and evaluating to True
    #  contrived_function returning False
    def test2(self):
        self.assertFalse(contrived_func(6))


if __name__ == '__main__':
    unittest.main(verbosity=2)