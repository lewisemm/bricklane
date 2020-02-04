from abc import ABCMeta, abstractproperty

class BasePaymentDetails(object):
    __metaclass__ = ABCMeta

    def get_source(self):
        return self.source

    def set_source(self, value):
        self.source = value

    def del_source(self):
        del self.source

    def get_status(self):
        return self.status

    def set_status(self, value):
        self.status = value

    def del_status(self):
        del self.status

    source = abstractproperty(get_source, set_source, del_source)
    status = abstractproperty(get_status, set_status, del_status)
