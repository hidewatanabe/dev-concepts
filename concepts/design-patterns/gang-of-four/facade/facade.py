class BillingSystem():
    def chargeClient(self, clientId:str) -> None:
        print(f'Generate billing for client {clientId}')

class MeteringSystem():
    def sendData(self, clientId: str) -> None:
        print(f'Sending metering data about client {clientId}')

class IdentitySystem():
    def identifyClient(self, clientId: str) -> None:
        print(f'Identifying client with clientId {clientId}')

class ManagementFacade():
    def __init__(self, billingSystem: BillingSystem, meteringSystem: MeteringSystem, identitySystem: IdentitySystem) -> None:
        self._billingSystem = billingSystem
        self._meteringSystem = meteringSystem
        self._identitySystem = identitySystem

    def clientEvent(self, clientId: str):
        results = []
        results.append('Facade initializes subsystems')
        results.append(self._identitySystem.identifyClient(clientId))
        results.append(self._meteringSystem.sendData(clientId))
        results.append(self._billingSystem.chargeClient(clientId))

class ClientService():
    def clientJourney(self, managementFacade: ManagementFacade) -> None:
        print('Starting client journey...')
        managementFacade.clientEvent('Teste')


if __name__ == '__main__':
    billingSystem = BillingSystem()
    meteringSystem = MeteringSystem()
    identitySystem = IdentitySystem()

    facade = ManagementFacade(billingSystem, meteringSystem, identitySystem)
    
    clientService = ClientService()
    clientService.clientJourney(facade)
