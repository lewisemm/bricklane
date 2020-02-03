from base import PaymentMethod

class Bank(PaymentMethod):

    bank_account_id = None
    processed = False
