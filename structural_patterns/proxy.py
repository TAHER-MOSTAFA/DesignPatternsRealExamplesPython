'''
A proxy controls access to the original object, 
allowing you to perform something either before or after the request gets through to the original object.

like lazy inialization or check cache first or controlling database accesss or logging

'''


from abc import ABC, abstractmethod


class AbstractQuery(ABC):
    @abstractmethod
    def get_data(self):
        pass

class RealQuery(AbstractQuery):
    def get_data(self):
        return "Data returned from a Real quey object"

class ProxyQuery(AbstractQuery):
    def __init__(self, q : RealQuery):
        self.q = q
        self.pervious_query_data = None
    
    def get_data(self):
        if self.pervious_query_data != None:
            return f"Data from pervious Query '{self.pervious_query_data}' "
        self.pervious_query_data = self.q.get_data()
        return self.pervious_query_data
    

if __name__ == '__main__':
    p = ProxyQuery(RealQuery())
    print(p.get_data())
    print(p.get_data())