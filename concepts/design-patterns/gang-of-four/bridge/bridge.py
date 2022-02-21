from abc import ABC, abstractmethod


class AWSProduct(ABC):
    @abstractmethod
    def create():
        pass

class CloudProvider:
    def __init__(self, product: AWSProduct) -> None:
        self.product = product

    def createOperation(self) -> None:
        return(f'CloudProvider: Base operation with:\n'
                f'{self.product.create()}')
    

class BillingCloudProvider(CloudProvider):
    def createOperation(self) -> None:
        return(f'CloudProvider: Billing operation with:\n'
                f'{self.product.create()}')


class AWSInstance(AWSProduct):
    def create(self) -> str:
        return('AWSInstance - create')

class AWSLoadBalancer(AWSProduct):
    def create(self) -> str:
        return('AWSLoadBalancer - create')

class CloudBackend():
    def create(self, cloudProvider: CloudProvider) -> None:
        print(cloudProvider.createOperation())

if __name__ == '__main__':
    cloudBackend = CloudBackend()
    
    instance = AWSInstance()
    cloudProvider = CloudProvider(instance)

    cloudBackend.create(cloudProvider)

    loadBalancer = AWSLoadBalancer()
    billingProvider = BillingCloudProvider(loadBalancer)

    cloudBackend.create(billingProvider)
