from base import BasePaymentDetails


class PaymentDetails(BasePaymentDetails):

    source = None
    status = None
    def __init__(self, source, data):
        self.source = source

        if self.source.lower() == "card":
            self.status = data.get("card_status")
            self.card_id = int(data["card_id"])
        elif self.source.lower() == "bank":
            self.status = "processed"
            self.bank_account_id = int(data["bank_account_id"])
