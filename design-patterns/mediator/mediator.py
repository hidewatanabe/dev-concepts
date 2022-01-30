from abc import ABC

class Mediator(ABC):
    def notify(self, sender:object, event: str) -> None:
        pass

class CloudProvider:
    def __init__(self, mediator: Mediator = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator

    def getInstances(self):
        self.mediator.notify(self, 'findInstance')
    
    def getBigQueriesInstances(self):
        self.mediator.notify(self, 'findBigQueryInstance')

class AWS(CloudProvider):
    def findInstance(self) -> None:
        print('find Instance in AWS')
        # self.mediator.notify(self, 'findInstance')
    
class Azure(CloudProvider):
    def findInstance(self) -> None:
        print('find instances in Azure')
        # self.mediator.notify(self, 'findInstance')

class GCP(CloudProvider):
    def findInstance(self) -> None:
        print('find instances in GCP')
        # self.mediator.notify(self, 'findInstance')

    def findBigQueryInstance(self) -> None:
        print('find Big Query instances in GCP')
        # self.mediator.notify(self, 'findBigQueryInstance')

class ConcreteMediator(Mediator):
    def __init__(self, aws: AWS, azure: Azure, gcp: GCP, provider: CloudProvider) -> None:
        self._aws = aws
        self._azure = azure
        self._gcp = gcp
        self._provider = provider
        self._aws.mediator = self
        self._azure.mediator = self
        self._gcp.mediator = self
        self._provider.mediator = self

    def notify(self, sender:object, event:str) -> None:
        if event == 'findBigQueryInstance':
            print('Mediator reacts on findBigQueryInstance from ' + sender.__class__.__name__ + ' and triggers following operations')
            self._gcp.findBigQueryInstance()
        if event == 'findInstance':
            print('Mediator reacts on findInstance from ' + sender.__class__.__name__ + ' and triggers following operations')
            self._aws.findInstance()
            self._azure.findInstance()
            self._gcp.findInstance()
        
if __name__ == '__main__':
    aws = AWS()
    azure = Azure()
    gcp = GCP()
    provider = CloudProvider()
    mediator = ConcreteMediator(aws, azure, gcp, provider)

    print('Client triggers findBigQueryInstance')
    provider.getBigQueriesInstances()

    print('Client triggers findInstance')
    provider.getInstances()
