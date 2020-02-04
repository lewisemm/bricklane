import unittest
from datetime import datetime

from bricklane_platform.models.payment import Payment
from bricklane_platform.models.details import PaymentDetails


class TestPayment(unittest.TestCase):

    def test_init(self):
        payment = Payment()

        self.assertIsNone(payment.customer_id)
        self.assertIsNone(payment.date)
        self.assertIsNone(payment.amount)
        self.assertIsNone(payment.fee)
        self.assertIsNone(payment.card_id)

    def test_init_with_card_data(self):

        data = {
            "amount": "2000",
            "card_id": "45",
            "card_status": "processed",
            "customer_id": "123",
            "date": "2019-02-01",
        }

        payment = Payment(data)

        self.assertEqual(payment.customer_id, 123)
        self.assertEqual(payment.date, datetime(2019, 2, 1))
        self.assertEqual(payment.amount, 1960)
        self.assertEqual(payment.fee, 40)

        payment_details = payment.payment_details

        self.assertIsInstance(payment_details, PaymentDetails)
        self.assertEqual(payment_details.card_id, 45)
        self.assertEqual(payment_details.status, "processed")

    def test_is_successful_card_declined(self):

        data = {
            "amount": "2000",
            "card_id": "45",
            "card_status": "declined",
            "customer_id": "123",
            "date": "2019-02-01",
        }

        payment = Payment(data)

        self.assertEqual(payment.customer_id, 123)
        self.assertEqual(payment.date, datetime(2019, 2, 1))
        self.assertEqual(payment.amount, 1960)
        self.assertEqual(payment.fee, 40)

        payment_details = payment.payment_details

        self.assertIsInstance(payment_details, PaymentDetails)
        self.assertEqual(payment_details.card_id, 45)
        self.assertEqual(payment_details.status, "declined")

    def test_is_successful_card_errored(self):

        data = {
            "amount": "2000",
            "card_id": "45",
            "card_status": "errored",
            "customer_id": "123",
            "date": "2019-02-01",
        }

        payment = Payment(data)

        self.assertEqual(payment.customer_id, 123)
        self.assertEqual(payment.date, datetime(2019, 2, 1))
        self.assertEqual(payment.amount, 1960)
        self.assertEqual(payment.fee, 40)

        payment_details = payment.payment_details

        self.assertIsInstance(payment_details, PaymentDetails)
        self.assertEqual(payment_details.card_id, 45)
        self.assertEqual(payment_details.status, "errored")

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

        payment_details = payment.payment_details

        self.assertIsInstance(payment_details, PaymentDetails)
        self.assertEqual(payment_details.bank_account_id, 45)
        self.assertTrue(payment_details.status)
