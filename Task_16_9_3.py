from Customer import Customer
from FinancialOperation import FinancialOperation
import datetime

customer1 = Customer("Aaron", "Paul")
customer2 = Customer("Jason", "Statham")

customer1.add_operation(FinancialOperation("Account topped up by online transfer", datetime.datetime(2021, 1, 10), "TOP_UP", 100.0))
customer1.add_operation(FinancialOperation("Pets food donation 20.0", datetime.datetime(2021, 1, 12), "PAYMENT", 20.0))
customer1.add_operation(FinancialOperation("Pets food donation 30.0", datetime.datetime(2021, 1, 13), "PAYMENT", 30.0))

customer2.add_operation(FinancialOperation("Account topped up by online transfer", datetime.datetime(2021, 2, 10), "TOP_UP", 100.0))
customer2.add_operation(FinancialOperation("Account topped up by online transfer", datetime.datetime(2021, 2, 11), "TOP_UP", 50.0))
customer2.add_operation(FinancialOperation("Pets food donation 70.0", datetime.datetime(2021, 2, 15), "PAYMENT", 60.0))
customer2.add_operation(FinancialOperation("Pets food donation 30.0", datetime.datetime(2021, 2, 16), "PAYMENT", 30.0))

customers = [customer1, customer2]

for customer in customers:
    print("Customer: {} {}, Balance: {}".format(customer.first_name, customer.last_name, customer.calculate_balance()))