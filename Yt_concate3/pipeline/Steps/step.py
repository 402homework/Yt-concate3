from abc import ABC
from abc import abstractmethod


class Step(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def process(self,data,inputs):    #增加input字典接受後來要用到的參數
        pass

class StepException(Exception):    #繼承Exception因此括號內要增加
    pass