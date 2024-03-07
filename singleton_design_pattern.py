

class SingletonGangOfFour:
    _instance = None

    def __init__(self, *args, **kwargs): # restricting the normal pathway of creating a class instance
        raise RuntimeError("Use instance method of class to get an instance")
    
    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
        return cls._instance


class SingletonPythonic:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SingletonPythonic, cls).__new__(cls)
        return cls._instance


if __name__=="__main__":
    singleton_one = SingletonGangOfFour.instance()
    singleton_two = SingletonGangOfFour.instance()
    assert id(singleton_one) == id(singleton_two)
    singleton_one = SingletonPythonic()
    singleton_two = SingletonPythonic()
    assert id(singleton_one) == id(singleton_two)

