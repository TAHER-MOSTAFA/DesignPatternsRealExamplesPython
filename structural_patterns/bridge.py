'''
A wise man once said "Using the bridge pattern is a good idea when you want to share an implementation among
multiple objects."

for example viewing a data in table
many models can return data and abstract deal with it and view it

another is to get data in backend
we can get it from database or cache 
and we can serialize these data with diffrent serializers

'''

from abc import ABC, abstractmethod


class Serializer(ABC):
    def __init__(self, Imp) -> None:
        self._imp = Imp
    
    @abstractmethod
    def operation_on_data(self):
        pass

class JsonSerializer(Serializer):
    def operation_on_data(self):
        print(f"we got data from {self._imp.__class__}, we will convert it to json")
        print(self._imp.data())




class DataFetcher(ABC):

    @abstractmethod
    def data(self):
        pass

class CacheFetcher(DataFetcher):
    def data(self):
        return "Data returned from Cache"

class DatabaseFetcher(DataFetcher):
    def data(self):
        return "Data returned from database"

if __name__ == '__main__':
    s = JsonSerializer(Imp=DatabaseFetcher())
    s.operation_on_data()