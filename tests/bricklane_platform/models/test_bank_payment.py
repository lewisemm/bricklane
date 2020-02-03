import unittest
from datetime import datetime

from bricklane_platform.models.payment import Payment
from bricklane_platform.models.bank import Bank

class TestBankPayment(unittest.TestCase):

    def test_init(self):
        payment = Payment()

        self.assertIsNone(payment.customer_id)
        self.assertIsNone(payment.date)
        self.assertIsNone(payment.amount)
        self.assertIsNone(payment.fee)

    def test_init_with_bank_data(self):

        data = {
            "amount": "2000",
            "bank_account_id": "45",
            "customer_id": "123",
            "date": "2019-02-01",
        }

        payment = Payment(data, "bank")

        self.assertEqual(payment.customer_id, 123)
        self.assertEqual(payment.date, datetime(2019, 2, 1))
        self.assertEqual(payment.amount, 1960)
        self.assertEqual(payment.fee, 40)

        bank = payment.bank

        self.assertIsInstance(bank, Bank)
        self.assertEqual(bank.bank_account_id, 45)
        self.assertTrue(bank.processed)

    def test_is_successful_bank_payment(self):
        bank = Bank()
        bank.processed = True
        payment = Payment(source="bank")
        payment.bank = bank

        self.assertTrue(payment.is_successful())

    def test_is_successful_bank_payment_not_processed(self):
        bank = Bank()
        payment = Payment(source="bank")
        payment.bank = bank

        self.assertFalse(payment.is_successful())