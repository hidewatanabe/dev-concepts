from abc import ABC, abstractmethod
from typing import List

class Observer(ABC):
    @abstractmethod
    def update(self, action) -> None:
        pass

class Action(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass

class CreateAction(Action):
    _context: str = None
    _action: str = 'create'
    _observers = List = []

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        print('Instance Action: Notifying observers...')
        for observer in self._observers:
            observer.update(self)

    def createUser(self) -> None:
        print('Create an user')
        self._context = 'user'
        print('Notifying the observers with context: ' + self._context)
        self.notify()

    def createInstance(self) -> None:
        print('Create an instance')
        self._context = 'instance'
        print('Notifying the observers with context: ' + self._context)
        self.notify()

class BillingObserver(Observer):
    def update(self, action: Action) -> None:
        if action._action == 'create':
            if action._context == 'instance':
                print('Adding billing issue for create instance.')
            if action._context == 'user':
                print('No action needed. Creating an user dont generate any billing issue.')

class TelemetryObserver(Observer):
    def update(self, action: Action) -> None:
        if action._action == 'create':
            if action._context == 'instance':
                print('Adding telemetry issue for create instance.')
            if action._context == 'user':
                print('Adding telemetry issue for create user.')

if __name__ == '__main__':
    action = CreateAction()

    billing = BillingObserver()
    telemetry = TelemetryObserver()

    action.attach(billing)
    action.attach(telemetry)

    action.createInstance()
    action.createUser()

    action.detach(billing)
    action.createUser()