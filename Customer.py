class Customer:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.operations = []

    def add_operation(self, financial_operation):
        self.operations.append(financial_operation)

    def calculate_balance(self):
        result = 0
        for operation in self.operations:
            if operation.operation_type == "TOP_UP":
                result = result + operation.amount
            else:
                result = result - operation.amount
        return result