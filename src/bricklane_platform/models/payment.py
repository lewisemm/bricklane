from decimal import Decimal
from dateutil.parser import parse

from bricklane_platform.models.details import PaymentDetails
from bricklane_platform.config import PAYMENT_FEE_RATE


class Payment(object):

    customer_id = None
    date = None
    amount = None
    fee = None
    card_id = None
    source = None

    def __init__(self, data=None, source="card"):

        self.source = source

        if not data:
            return

        self.customer_id = int(data["customer_id"])
        self.date = parse(data["date"])

        total_amount = Decimal(data["amount"])
        self.fee = total_amount * PAYMENT_FEE_RATE
        self.amount = total_amount - self.fee

        self.payment_details = PaymentDetails(source, data)

    def is_successful(self):
        return self.payment_details.status == "processed"
