import unittest
from credit_card_validator import credit_card_validator

class TestCCValidator(unittest.TestCase):

    # This test uses a valid Visa prefix and length, but has an invalid check digit,
    # so it should be an invalid credit card number
    # The assertion is checking that the returned value from the validator is False
    def test1(self):
        self.assertFalse(credit_card_validator("4624748233249080"))

    # This test uses a valid Visa prefix and length and it has a valid check digit,
    # so it should be an valid credit card number
    # The assertion is checking that the returned value from the validator is True
    def test2(self):
        self.assertTrue(credit_card_validator("4624748233249780"))

if __name__ == '__main__':
    unittest.main(verbosity=2)