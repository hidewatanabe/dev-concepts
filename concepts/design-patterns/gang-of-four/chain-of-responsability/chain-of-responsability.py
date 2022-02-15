

from abc import ABC, abstractclassmethod, abstractmethod
from typing import Optional

class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: any):
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class BaseHandler(Handler):
    _nextHandler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._nextHandler = handler

        return handler

    def handle(self, request: any) -> str:
        if self._nextHandler:
            return self._nextHandler.handle(request)
        return None


class LoginHandler(BaseHandler):
    def handle(self, request: any) -> str:
        if not request['login']:
            return 'LoginHandler: User is not logged in'
        return super().handle(request)

class AdimplencyHandler(BaseHandler):
    def handle(self, request: any) -> str:
        if not request['adimplency']:
            return 'AdimplencyHandler: User has some bill to pay'
        return super().handle(request)

class CreditHandler(BaseHandler):
    def handle(self, request: any) -> str:
        if not request['creditAvailable']:
            return 'CreditHandler: User dont have enough credits to do this action!'
        return super().handle(request)

def createServiceOrder(handler: Handler) -> None:
    request1 = {'login': False, 'adimplency': False, 'creditAvailable': False}
    request2 = {'login': True, 'adimplency': False, 'creditAvailable': False}
    request3 = {'login': True, 'adimplency': True, 'creditAvailable': False}
    request4 = {'login': True, 'adimplency': True, 'creditAvailable': True}

    for request in [request1, request2, request3, request4]:
        print('Creating Service Order for:' + str(request))
        result = handler.handle(request)
        if result:
            print(f'Request result: {result}')
            print()
        else:
            print('OS Created! Validation OK!')

if __name__ == '__main__':
    loginHandler = LoginHandler()
    adimplencyHandler = AdimplencyHandler()
    creditHandler = CreditHandler()

    loginHandler.set_next(adimplencyHandler).set_next(creditHandler)

    print('-------------------------------------------')
    print('Chain sequency: login, adimplency and credit')
    print('-------------------------------------------')

    createServiceOrder(loginHandler)

    print('===========================================')

    print('-------------------------------------------')
    print('Subchain sequency: adimplency and credit')
    print('-------------------------------------------')

    createServiceOrder(adimplencyHandler)