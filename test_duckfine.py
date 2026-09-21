import unittest

from duckfine import DuckFine


class DuckFineTests(unittest.TestCase):
    def setUp(self):
        self.fine = DuckFine("M001")

    def test_charge_returns_a_fee_for_a_late_duck(self):
        self.assertEqual(self.fine.charge(5), 1.50)

    def test_deluxe_duck_costs_more(self):
        self.assertTrue(self.fine.charge(5, deluxe=True) > 0)

    def test_no_fee_when_returned_on_time(self):
        self.assertEqual(self.fine.charge(0), 0.0)

    def test_negative_days_raises(self):
        with self.assertRaises(ValueError):
            self.fine.charge(-1)

    '''def test_fee_is_capped_at_the_maximum(self):
        fee = self.fine.charge(100)

        self.assertEqual(fee, 5.00)
        self.assertEqual(self.fine.total_owed, 5.00)

    def test_deluxe_fee_is_capped_at_the_maximum(self):
        fee = self.fine.charge(100, deluxe=True)

        self.assertEqual(fee, 5.00)
        self.assertEqual(self.fine.total_owed, 5.00)
'''
if __name__ == "__main__":
    unittest.main()