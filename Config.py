from Dealership.Invoice.InvoiceCatalog import InvoiceCatalog
from Dealership.Invoice.Order.OrderCatalog import OrderCatalog
from Dealership.Profiles.Customer.CustomerDirectory import CustomerDirectory
from Dealership.Profiles.SalesPerson.SalesPersonDirectory import SalesPersonDirectory
from VehicleDealership import VehicleDealership
from Dealership.Inventory.InventoryCatalog import InventoryCatalog
from Dealership.Inventory.VehicleCatalog import VehicleCatalog
from Dealership.Inventory.VehicleFeatures.VehicleSize import VehicleSize
from Dealership.Inventory.VehicleFeatures.VehicleColor import VehicleColor
from Dealership.Inventory.VehicleFeatures.VehicleMake import VehicleMake
import datetime


class Config:

    @staticmethod
    def populate_initial_data():
        vehicle_catalog = VehicleCatalog()
        inventory_catalog = InventoryCatalog()
        order_catalog = OrderCatalog()
        invoice_catalog = InvoiceCatalog()
        sales_person_directory = SalesPersonDirectory()
        customer_directory = CustomerDirectory()

        VehicleDealership.add_inventory(30, VehicleMake.TOYOTA, 'Corolla', 2015, 16500, VehicleSize.MEDIUM, VehicleColor.BLACK)
        VehicleDealership.add_inventory(30, VehicleMake.TOYOTA, 'Corolla', 2015, 16500, VehicleSize.MEDIUM, VehicleColor.BLACK)
        VehicleDealership.add_inventory(3, VehicleMake.TOYOTA, 'Corolla', 2016, 17500, VehicleSize.MEDIUM, VehicleColor.BLUE)
        VehicleDealership.add_inventory(3, VehicleMake.TOYOTA, 'Corolla', 2017, 19500, VehicleSize.MEDIUM, VehicleColor.BLACK)
        VehicleDealership.add_inventory(3, VehicleMake.TOYOTA, 'Corolla', 2017, 19000, VehicleSize.MEDIUM, VehicleColor.WHITE)
        VehicleDealership.add_inventory(3, VehicleMake.TOYOTA, 'Camry', 2015, 21000, VehicleSize.MEDIUM, VehicleColor.BLACK)
        VehicleDealership.add_inventory(3, VehicleMake.TOYOTA, 'Camry', 2016, 22000, VehicleSize.MEDIUM, VehicleColor.BLUE)
        VehicleDealership.add_inventory(3, VehicleMake.TOYOTA, 'Camry', 2017, 24500, VehicleSize.MEDIUM, VehicleColor.BLACK)
        VehicleDealership.add_inventory(3, VehicleMake.TOYOTA, 'Camry', 2017, 24000, VehicleSize.MEDIUM, VehicleColor.WHITE)
        VehicleDealership.add_inventory(3, VehicleMake.HONDA, 'Civic', 2015, 15500, VehicleSize.MEDIUM, VehicleColor.BLACK)
        VehicleDealership.add_inventory(3, VehicleMake.HONDA, 'Civic', 2016, 16500, VehicleSize.MEDIUM, VehicleColor.BLUE)
        VehicleDealership.add_inventory(3, VehicleMake.HONDA, 'Civic', 2017, 18500, VehicleSize.MEDIUM, VehicleColor.BLACK)
        VehicleDealership.add_inventory(3, VehicleMake.HONDA, 'Civic', 2017, 18000, VehicleSize.MEDIUM, VehicleColor.WHITE)
        VehicleDealership.add_inventory(3, VehicleMake.HONDA, 'Accord', 2015, 22000, VehicleSize.MEDIUM, VehicleColor.BLACK)
        VehicleDealership.add_inventory(3, VehicleMake.HONDA, 'Accord', 2016, 23000, VehicleSize.MEDIUM, VehicleColor.BLUE)
        VehicleDealership.add_inventory(3, VehicleMake.HONDA, 'Accord', 2017, 26500, VehicleSize.MEDIUM, VehicleColor.BLACK)
        VehicleDealership.add_inventory(3, VehicleMake.HONDA, 'Accord', 2017, 26000, VehicleSize.MEDIUM, VehicleColor.WHITE)
        VehicleDealership.add_inventory(3, VehicleMake.AUDI, 'A3', 2017, 35000, VehicleSize.MEDIUM, VehicleColor.BLACK)
        VehicleDealership.add_inventory(3, VehicleMake.AUDI, 'A4', 2017, 38000, VehicleSize.MEDIUM, VehicleColor.BLUE)
        VehicleDealership.add_inventory(3, VehicleMake.AUDI, 'A5', 2017, 42000, VehicleSize.MEDIUM, VehicleColor.BLACK)
        VehicleDealership.add_inventory(3, VehicleMake.AUDI, 'A6', 2017, 45000, VehicleSize.MEDIUM, VehicleColor.WHITE)
        VehicleDealership.add_inventory(3, VehicleMake.AUDI, 'A7', 2017, 52000, VehicleSize.MEDIUM, VehicleColor.BLACK)
        VehicleDealership.add_inventory(3, VehicleMake.AUDI, 'A3', 2015, 30000, VehicleSize.MEDIUM, VehicleColor.BLUE)
        VehicleDealership.add_inventory(3, VehicleMake.AUDI, 'A3', 2016, 27000, VehicleSize.MEDIUM, VehicleColor.BLACK)
        VehicleDealership.add_inventory(3, VehicleMake.AUDI, 'A4', 2016, 35000, VehicleSize.MEDIUM, VehicleColor.WHITE)
        VehicleDealership.add_inventory(3, VehicleMake.DODGE, 'Challenger', 2017, 35000, VehicleSize.MEDIUM, VehicleColor.BLACK)
        VehicleDealership.add_inventory(3, VehicleMake.DODGE, 'Charger', 2017, 38000, VehicleSize.MEDIUM, VehicleColor.BLUE)
        VehicleDealership.add_inventory(3, VehicleMake.DODGE, 'Caliber', 2017, 42000, VehicleSize.MEDIUM, VehicleColor.BLACK)
        VehicleDealership.add_inventory(3, VehicleMake.DODGE, 'Journey', 2017, 45000, VehicleSize.MEDIUM, VehicleColor.WHITE)
        VehicleDealership.add_inventory(3, VehicleMake.DODGE, 'Lancer', 2017, 52000, VehicleSize.MEDIUM, VehicleColor.BLACK)
        VehicleDealership.add_inventory(3, VehicleMake.DODGE, 'Dynasty', 2015, 30000, VehicleSize.MEDIUM, VehicleColor.BLUE)
        VehicleDealership.add_inventory(3, VehicleMake.DODGE, 'Interpid', 2016, 27000, VehicleSize.MEDIUM, VehicleColor.BLACK)
        VehicleDealership.add_inventory(3, VehicleMake.DODGE, 'Avenger', 2016, 35000, VehicleSize.MEDIUM, VehicleColor.WHITE)

        # adding sales person
        vehicle_list = set()
        person = VehicleDealership.create_profile('Riti', 'Bahlani',
                                                  datetime.datetime.strptime('05/15/1975', '%m/%d/%Y'),45000, 'f',
                                                  '40 Newport Parkway', '2505', 'Jersey City', 'NJ', 'USA', 7310, '',
                                                  'riti@gmail.com', '543-125-6738', 'KLM291HM', 'IND', vehicle_list)
        sales_person = sales_person_directory.add_sales_person(person)

        # adding customer and placing order
        vehicle_list = set()
        for v in vehicle_catalog.vehicle_list:
            if v.id == 1 or v.id == 10 or v.id == 15 or v.id == 25:
                vehicle_list.add(v)
                if v.id == 1:
                    vehicle = v
        person = VehicleDealership.create_profile('Manish', 'Gajare',
                                                  datetime.datetime.strptime('05/15/1991', '%m/%d/%Y'), 85000, 'm',
                                                  '114 Longwood Avenue', '5', 'Brookline', 'MA', 'USA', 2446,
                                                  '2028305422', 'manishgajare@gmail.com', '543-857-9012', 'KLM1041G',
                                                  'IND', vehicle_list)
        customer = customer_directory.add_customer(person)
        for i in inventory_catalog.inventory_list:
            if i.vehicle == vehicle:
                inventory_item = i
        order = order_catalog.add_order(customer, sales_person, inventory_item, inventory_item.price)
        invoice_catalog.add_invoice(order)

        # adding customer and placing order
        vehicle_list = set()
        for v in vehicle_catalog.vehicle_list:
            if v.id == 1 or v.id == 2 or v.id == 17 or v.id == 15:
                vehicle_list.add(v)
                if v.id == 1:
                    vehicle = v
        person = VehicleDealership.create_profile('Yash', 'Kochar',
                                                  datetime.datetime.strptime('05/15/1989', '%m/%d/%Y'), 80000, 'm',
                                                  '114 Longwood Avenue', '5', 'Brookline', 'MA', 'USA', 2446,
                                                  '7583276666', 'yash@gmail.com', '543-857-7436', 'KLM456HM',
                                                  'IND', vehicle_list)
        customer = customer_directory.add_customer(person)
        for i in inventory_catalog.inventory_list:
            if i.vehicle == vehicle:
                inventory_item = i
        order = order_catalog.add_order(customer, sales_person, inventory_item, inventory_item.price)
        invoice_catalog.add_invoice(order)

        # adding customer and placing order
        vehicle_list = set()
        for v in vehicle_catalog.vehicle_list:
            if v.id == 7 or v.id == 9 or v.id == 8 or v.id == 2:
                vehicle_list.add(v)
                if v.id == 7:
                    vehicle = v
        person = VehicleDealership.create_profile('Ronak', 'Massand',
                                                  datetime.datetime.strptime('05/15/1992', '%m/%d/%Y'), 90000, 'm',
                                                  '114 Longwood Avenue', '5', 'Brookline', 'MA', 'USA', 2446,
                                                  '8473620986', 'ronak@gmail.com', '543-857-1025', 'KLM34HLL',
                                                  'IND', vehicle_list)
        customer = customer_directory.add_customer(person)
        for i in inventory_catalog.inventory_list:
            if i.vehicle == vehicle:
                inventory_item = i
        order = order_catalog.add_order(customer, sales_person, inventory_item, inventory_item.price)
        invoice_catalog.add_invoice(order)

        # adding customer and placing order
        vehicle_list = set()
        for v in vehicle_catalog.vehicle_list:
            if v.id == 13 or v.id == 23 or v.id == 19 or v.id == 30:
                vehicle_list.add(v)
                if v.id == 13:
                    vehicle = v
        person = VehicleDealership.create_profile('Prashant', 'Iyer',
                                                  datetime.datetime.strptime('05/15/1991', '%m/%d/%Y'), 85000, 'm',
                                                  '114 Longwood Avenue', '5', 'Brookline', 'MA', 'USA', 2446,
                                                  '9286772351', 'prashant@gmail.com', '543-857-6734', 'KLM97G3J',
                                                  'IND', vehicle_list)
        customer = customer_directory.add_customer(person)
        for i in inventory_catalog.inventory_list:
            if i.vehicle == vehicle:
                inventory_item = i
        order = order_catalog.add_order(customer, sales_person, inventory_item, inventory_item.price)
        invoice_catalog.add_invoice(order)
