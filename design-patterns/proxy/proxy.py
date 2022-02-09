from abc import ABC, abstractmethod


class CloudProvider(ABC):
    @abstractmethod
    def request(self) -> None:
        pass

class AWS(CloudProvider):
    def request(self) -> None:
        print("Handling request as AWS")

class Proxy(CloudProvider):
    def __init__(self, aws: AWS) -> None:
        self._aws = aws

    def checkAccess(self) -> bool:
        print("Proxy: Validating access...")
        return True

    def logAccess(self) -> None:
        print("Proxy: Logging the time of request.", end="")

    def request(self):
        if self.checkAccess():
            self._aws.request()
            self.logAccess()

def clientCode(cloudProvider: CloudProvider) -> None:
    cloudProvider.request()

if __name__ == '__main__':
    aws = AWS()
    clientCode(aws)

    print("")

    proxy = Proxy(aws)
    clientCode(proxy)