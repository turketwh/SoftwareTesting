import unittest
import random
from max_of_list import max_of_list


class TestCase(unittest.TestCase):
    pass


def build_test_func(expected, test_case, func_under_test, message):
    def test(self):
        result = func_under_test(test_case)
        self.assertEqual(expected, result, message.format(test_case, expected, result))
    return test


def generate_data():
    # TODO: Choose a random length of input list per guidelines in assignment document
    list_length = ?????
    # TODO: Chose max_value for list per guidelines in assignment document
    max_value = ?????
    # TODO: Choose where to put max value per guidelines in assignment document
    max_index = ?????
    # Initialize the list to be all zeros
    list_to_test = [0]*list_length
    # TODO: Set data in each spot per guidelines in assignment document
    # ?????
    # Uncommenting the next line will show you the list you generated
    # print(str(max_value) + " -> " + str(max_index) + " -> " + str(list_to_test))
    return max_value, list_to_test


def generate_test_cases():
    random.seed(12345)
    # TODO: Change this value to have more tests run (no more than 100 should be needed)
    tests_to_generate = 5
    # for index in range(X) iterates over integers from 0 to X-1 inclusive
    for index in range(tests_to_generate):
        expected, data_list = generate_data()
        message = 'Test case: {}, Expected: {}, Result: {}'
        new_test = build_test_func(expected, data_list, max_of_list, message)
        # `test_{}'.format(index) replaces {} with the number held by index
        # in the string test_{}
        setattr(TestCase, 'test_{}'.format(index), new_test)


generate_test_cases()
if __name__ == '__main__':
    unittest.main(verbosity=2)
