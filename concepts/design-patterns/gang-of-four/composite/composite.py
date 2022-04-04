
class Product():
    def operation(self) -> str:
        pass

class VM(Product):
    def operation(self) -> str:
        return "Instanciating an instance"

# Esse é o decorator - comportamento adicional sem necessariamente ser por herança
class BaseDecorator(Product):
    _product: Product = None

    def __init__(self, product: Product) -> None:
        self._product = product

    @property
    def product(self) -> Product:
        return self._product

    def operation(self) -> str:
        return self._product.operation()

class BillingDecorator(BaseDecorator):
    def operation(self) -> str:
        return f"Adding billing issue in action: {self.product.operation()}"

class LogDecorator(BaseDecorator):
    def operation(self) -> str:
        return f"Sending log info from action: {self.product.operation()}"

def create(product: Product) -> None:
    print(f"Create a product: {product.operation()}")

if __name__ == "__main__":
    vm = VM()
    print('-------------------------------------------')
    print("Starting creating instance process...")
    print('-------------------------------------------')
    
    create(vm)
    
    print()
    print('===========================================')
    print()

    print('-------------------------------------------')
    print("Adding billing decorator in create VM action")
    print('-------------------------------------------')
    billing = BillingDecorator(vm)
    create(billing)

    print('-------------------------------------------')
    print("Adding log decorator in billing decorator")
    print('-------------------------------------------')
    logging = LogDecorator(billing)
    create(logging)
    