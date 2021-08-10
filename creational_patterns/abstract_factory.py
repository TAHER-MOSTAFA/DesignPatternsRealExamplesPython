'''
Abstract factory is same idea of factory pattern it returns a object of class
but not only one and those new objects are compatible together
Back to our Example of sending that notification 
we may use special service to send that message for every type

conculsion start with factory then go abstract
'''

from abc import ABC, abstractmethod


class Message(ABC):
    
    def __init__(self, receiver, text):
        self.receiver = receiver
        self.text = text
    
    @abstractmethod
    def create_message(self, text):
        pass

class EmailMessage(Message):

    def create_message(self):
        return f"<h1> Dear {self.receiver} ,, {self.text} </h1>"
    

class MobileMessage(Message):
    
    def create_message(self):
        return f"Dear {self.receiver} ,, {self.text}"


class Service(ABC):
    def __init__(self, msg : Message) -> None:
        self.msg = msg

    @abstractmethod
    def send(self):
        pass


class EmailService(Service):
    def send(self) -> None:
        print(f"email sent {self.msg.text} to {self.msg.receiver}") 


class MobileService(Service):
    def send(self) -> None:
        print(f"Mobile notification sent {self.msg.text} to {self.msg.receiver}")


# Factories
class AbstractFactory(ABC):
    @abstractmethod
    def get_message():
        pass
    @abstractmethod
    def get_service():
        pass

class EmailAbstractFactory(AbstractFactory):
    
    @staticmethod
    def get_message(receiver, text):
        # Handle Exceptions or add wrapper
        return EmailMessage(receiver, text)
    
    @staticmethod
    def get_service(msg: Message):
        return EmailService(msg)

if __name__ == '__main__':
    email_msg = EmailAbstractFactory.get_message("taher.mostafa808@gmail.com", "test")
    email_service = EmailAbstractFactory.get_service(email_msg)
    email_service.send()
