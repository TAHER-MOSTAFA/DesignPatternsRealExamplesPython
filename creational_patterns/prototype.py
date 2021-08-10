'''
what if we wanted to forward message but keeping the original one as we will change receiver
here comes this pattern to solve it

'''
import copy

class Receiver:
    def __init__(self, name) -> None:
        self.name = name

class Message:
    # we may add registery for our cloned objs but I want to keep it simple
    # it is not important in our case
    # also we can use __copy__ and __deepcopy__ for custom copies when using copy with this class
    
   
    def __init__(self, receiver, text, subject='No subject') -> None:
        self.receiver = receiver
        self.text = text
        self.subject = subject

    def create_message(self):
        return f"<h1> Dear {self.receiver} ,, {self.text} </h1>"
# since it is built-in feature in python 

# we want to clone msg but change receiver right?

def clone_msg(msg : Message, receiver: Receiver):
    # in this case only one related class and we will change it 
    # we could use shallow copy instead
    cloned_msg = copy.deepcopy(msg)
    cloned_msg.receiver = receiver
    return cloned_msg


if __name__ == "__main__":
    rcvr1 = Receiver("rcvr1") 
    rcvr2 = Receiver("rcvr2")
    msg = Message(rcvr1, "message","Hi")
    cloned_msg = clone_msg(msg, rcvr2)
    
    
    print(id(msg) == id(cloned_msg))
    print(cloned_msg.receiver.name)