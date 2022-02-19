
from abc import ABC, abstractmethod
from datetime import datetime

class CloudManagement(ABC):
    def createAccount(self, username: str, billingType: str) -> None:
        userdata = self.getUserData(username)
        self.getBillingData(userdata, billingType)
        self.createAccountInCloudProvider(userdata)
        self.createUserInCloudProvider(userdata)
        self.createProjectInCloudProvider(userdata)
        self.getUserDataInCloudProvider(userdata)

    def getUserData(self, username:str) -> str:
        print(f'Getting data from user: {username}')
        result = {'username':username, 'date':datetime.today()}
        return result

    def getBillingData(self, userdata:dict, billingType:str) -> None:
        print(f'Getting billingType from user: {userdata["username"]}')
        userdata['billingType'] = billingType

    @abstractmethod
    def createAccountInCloudProvider(self, userdata:dict) -> None:
        print('CloudManagement: Using client info to create an account in selected CloudProvider.')
    
    @abstractmethod
    def createUserInCloudProvider(self, userdata:dict) -> None:
        print('CloudManagement: Using client info to create an user in selected CloudProvider.')
    
    @abstractmethod
    def createProjectInCloudProvider(self, userdata:dict) -> None:
        print('CloudManagement: Using client info to create a project in selected CloudProvider.')

    @abstractmethod
    def getUserDataInCloudProvider(self, userdata:dict) -> None:
        print('CloudManagement: Using client filter to get info in selected CloudProvider.')


class AWS(CloudManagement):
    def createAccountInCloudProvider(self, userdata: dict) -> None:
        print(f'Creating an account in AWS for {userdata["username"]}')
        userdata['cloudProvider'] = 'AWS'
        userdata['region'] = 'SA-EAST-1'
    
    def createUserInCloudProvider(self, userdata: dict) -> None:
        print(f'Creating an user in AWS for {userdata["username"]}')
        userdata['cloudProviderUser'] = 'AWS.'+userdata['username']

    def createProjectInCloudProvider(self, userdata: dict) -> None:
        print(f'Creating a project in AWS for {userdata["username"]}')
        userdata['cloudProviderProject'] = 'AWS.'+userdata['username']+'.project'
    
    def getUserDataInCloudProvider(self, userdata: dict) -> None:
        print(f'Project data: {userdata}')


class Azure(CloudManagement):
    def createAccountInCloudProvider(self, userdata: dict) -> None:
        print(f'Creating an account in Azure for {userdata["username"]}')
        userdata['cloudProvider'] = 'Azure'
        userdata['region'] = 'Brazil South'
    
    def createUserInCloudProvider(self, userdata: dict) -> None:
        print(f'Creating an user in Azure for {userdata["username"]}')
        userdata['cloudProviderUser'] = 'Azure.'+userdata['username']

    def createProjectInCloudProvider(self, userdata: dict) -> None:
        print(f'Creating a project in Azure for {userdata["username"]}')
        userdata['cloudProviderProject'] = 'Azure.'+userdata['username']+'.project'
    
    def getUserDataInCloudProvider(self, userdata: dict) -> None:
        print(f'Project data: {userdata}')

class GCP(CloudManagement):
    def createAccountInCloudProvider(self, userdata: dict) -> None:
        print(f'Creating an account in GCP for {userdata["username"]}')
        userdata['cloudProvider'] = 'GCP'
        userdata['region'] = 'southamerica-east1'
    
    def createUserInCloudProvider(self, userdata: dict) -> None:
        print(f'Creating an user in GCP for {userdata["username"]}')
        userdata['cloudProviderUser'] = 'GCP.'+userdata['username']

    def createProjectInCloudProvider(self, userdata: dict) -> None:
        print(f'Creating a project in Azure for {userdata["username"]}')
        userdata['cloudProviderProject'] = 'GCP.'+userdata['username']+'.project'
    
    def getUserDataInCloudProvider(self, userdata: dict) -> None:
        print(f'Project data: {userdata}')

class ClientService():
    def createEnvironment(self, cloudManagement: CloudManagement, username:str, billingType:str) -> None:
        print('Doing some previous validation before creating the client environment in cloud provider...')
        cloudManagement.createAccount(username, billingType)

if __name__ == '__main__':
    clientService = ClientService()
    print('-------------------------------------------')
    print('AWS Providing...')
    print('-------------------------------------------')
    clientService.createEnvironment(AWS(), 'Wata', None)


    print('-------------------------------------------')
    print('Azure Providing...')
    print('-------------------------------------------')
    clientService.createEnvironment(Azure(), 'Wata', 'Slip')


    print('-------------------------------------------')
    print('GCP Providing...')
    print('-------------------------------------------')
    clientService.createEnvironment(GCP(), 'Wata', 'CreditCard')