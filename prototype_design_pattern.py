from abc import ABC, abstractmethod
import copy


class Prototype(ABC):
    def __init__(self):
        self.weight = None
        self.color = None

    @abstractmethod    
    def clone(self):
        pass


class Camaro(Prototype):
    def __init__(self, drive: str):
        super().__init__()
        self.weight = 1500
        self.color = "red"
        self.drive = drive
    
    def clone(self):
        return copy.deepcopy(self)


if __name__=="__main__":
    car_list = []
    camaro = Camaro(drive="diesel")
    for _ in range(10):
        car_list.append(camaro.clone())
    print(car_list)

        
