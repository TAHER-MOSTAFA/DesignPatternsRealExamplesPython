# Imagine we have an app thaht notify users for messages but there is 2 types
# First by Email, Second by mobile notification 
# so what if we wanted to notify by only one of them only or add new one -SMS maybe-
# it would be hard to implement and use too many if/else statements
# another solution to use dictionary
# another solution to use creator and product classes

from abc import ABC, abstractmethod


class Message(ABC):
    
    def __init__(self, receiver, text):
        self.receiver = receiver
        self.text = text
    
    @abstractmethod
    def create_message(self, text):
        pass
    @abstractmethod
    def send(self):
        pass

class EmailMessage(Message):
   
    def create_message(self):
        return f"<h1> Dear {self.receiver} ,, {self.text} </h1>"
    
    def send(self):
        print(f"email sent {self.create_message()}")

class MobileMessage(Message):
    
    def create_message(self):
        return f"Dear {self.receiver} ,, {self.text}"

    def send(self):
        print(f"Mobile notification sent {self.create_message()}")


class MessageFactory:
    # here we can use dictionary or if/else or use function instead 
    # but we will have to make a wrapper for exceptions

    def Email(text: str, receiver:str) -> Message:
        #handle exceptions
        return EmailMessage(text, receiver)

    def Mobile(text: str, receiver: str) -> Message:
        return MobileMessage(text, receiver)

if __name__ == '__main__':

    obj1 = MessageFactory.Email("test", "Taher.Mostafa808@gmail.com")
    obj1.send()

    obj2 = MessageFactory.Mobile("test", "01097004552")
    obj2.send()
