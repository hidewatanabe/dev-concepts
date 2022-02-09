# Cada classe representa um microserviço dentro de uma arquitetura

import time

class CloudPlatform():
    def getCloudUsers(self):
        print('Getting Cloud User from provider')

class CloudProvider():
    def getCloudUsers(self):
        time.sleep(2)
        print("Getting Cloud Users from database")

class CircuitBreaker():
    def __init__(self) -> None:
        # True é fechado e False é aberto
        self._circuitState = True
        self._invocationTimeout = 0.01
        self._failureThreshold = 5
        self._resetTimeout = 0.1
        self._failureCount = 0

    @property
    def failureThreshold(self):
        return self._failureThreshold

    @property
    def failureCount(self):
        return self._failureCount
    
    @failureCount.setter
    def failureCount(self, failureCount: int):
        self._failureCount = failureCount

    @property
    def invocationTimeout(self):
        return self._invocationTimeout

    @property
    def circuitState(self):
        return self._circuitState
    
    @circuitState.setter
    def circuitState(self, circuitState: bool) -> None:
        self._circuitState = circuitState

    def resetCircuitBreaker(self):
        self.failureCount(0)       

    def validateMonitoring(self, elapsedTime):
        if self.invocationTimeout < elapsedTime:
            self.failureCount(self.failureCount()+1)
        if self.failureCount >= self.failureThreshold():
            self.circuitState = False
        

    def callDecorator(self, func):
        start = time.time()
        func()
        stop = time.time()
        elapsedTime = stop - start
        print('Time elapsed: ' + str(elapsedTime))
        self.validateMonitoring(elapsedTime)
        return elapsedTime

    def callProvider(self):
        if self.circuitState:
            provider = CloudProvider()
            self.callDecorator(provider.getCloudUsers)
        else:
            print('Circuito está aberto! Aguardando o serviço chamado voltar a sua normalidade...')

    def getProviderState(self):
        if not self.circuitState:
            provider = CloudProvider()
            provider.getCloudUsers
    

if __name__ == '__main__':
    circuitBreaker = CircuitBreaker()
    circuitBreaker.callProvider()
        


