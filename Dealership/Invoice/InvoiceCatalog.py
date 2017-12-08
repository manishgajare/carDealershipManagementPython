import threading
from Dealership.Invoice.Invoice import Invoice


class InvoiceCatalog:
    __instance = None
    __lock = threading.Lock()
    __invoice_list = None
    __invoice_count_for_id = None

    def __new__(cls):
        if cls.__instance is None:
            with cls.__lock:
                if cls.__instance is None:
                    cls.__instance = super(InvoiceCatalog, cls).__new__(cls)
                    cls.__instance.__initialized = False
        return cls.__instance

    def __init__(self):
        if self.__initialized:
            return
        self.__invoice_list = set()
        self.__invoice_count_for_id = 1
        self.__initialized = True

    def get_invoice_list(self):
        return self.__invoice_list

    def add_invoice(self, order):
        invoice = Invoice(self.__invoice_count_for_id, order)
        self.__invoice_count_for_id += 1
        self.__invoice_list.add(invoice)
        return invoice

    def toString(self):
        invoice_catalog_string = ''
        print('Invoice Catalog -> ')
        for invoice in self.__invoice_list:
            invoice_catalog_string = invoice_catalog_string + invoice.toString() + '\n'
        return invoice_catalog_string