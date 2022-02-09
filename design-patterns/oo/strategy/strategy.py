from abc import ABC, abstractmethod

class CloudProvider(ABC):
    @abstractmethod
    def getBillingData(self):
        pass

class AWS(CloudProvider):
    def getBillingData(self):
        print('Getting AWS Billing info...')

class Azure(CloudProvider):
    def getBillingData(self):
        print('Getting Azure Billing info...')

class GCP(CloudProvider):
    def getBillingData(self):
        print('Getting GCP billing info...')

class Cloud():
    def __init__(self, cloudProvider:CloudProvider) -> None:
        self._cloudProvider = cloudProvider

    @property
    def cloudProvider(self) -> CloudProvider:
        return self._cloudProvider

    @cloudProvider.setter
    def cloudProvider(self, cloudProvider:CloudProvider) -> None:
        self._cloudProvider = cloudProvider

    def getBilling(self) -> None:
        print("Getting billing data from some CloudProvider")
        self._cloudProvider.getBillingData()

if __name__ == '__main__':
    cloud = Cloud(AWS())
    cloud.getBilling()

    print()

    cloud.cloudProvider = Azure()
    cloud.getBilling()

    print()

    cloud.cloudProvider = GCP()
    cloud.getBilling()