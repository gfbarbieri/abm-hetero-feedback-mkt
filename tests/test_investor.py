import unittest
from unittest.mock import MagicMock
from src.models.investor import Investor

class TestFirm(unittest.TestCase):

    def setUp(self):
        """
        Set up a Firm instance before each test method.
        """

        self.mock_model = MagicMock()
        self.firm = Investor(self.mock_model)

    def test_setup(self):
        """
        """
        pass

    def trade(self):
        """
        """
        pass

    def update_threshold(self):
        """
        """
        pass

    def update_strategy(self):
        """
        """
        pass

if __name__ == '__main__':
    unittest.main()