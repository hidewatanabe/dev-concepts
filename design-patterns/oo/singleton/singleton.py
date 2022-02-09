class CloudClientMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

    
class CloudClient(metaclass=CloudClientMeta):
    def get_unique_client(self):
        pass

if __name__ == '__main__':
    s1 = CloudClient()
    s2 = CloudClient()

    print('CloudClient s1: ' + str(id(s1)))
    print('CloudClinet s2: ' + str(id(s2)))

    if id(s1) == id(s2):
        print('Ids iguais - Singleton funcionou!')
    else:
        print('Ids diferentes - Singleton não funcionou!')