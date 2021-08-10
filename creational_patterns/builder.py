'''
builder pattern is used when we want to create object but not at one time 
instead we are building it step by step
for example Email messge it have receiver text html_text cc image attachement subject
not all are necessary in every email , they change so we build the message object in many steps

'''

class EmailMessage:
    def __init__(self) -> None:
        self.receiver = None
        self.cc = None
        self.text = None
        self.html_text = None
        self.image = None
        self.subject = 'no-subject'
        self.attachement = None

class EmailBuilder:
    def __init__(self) -> None:
        self._msg = EmailMessage()

    def add_text(self, text: str):
        self._msg.text = text
        print("text added")

    def add_subject(self, subject: str):
        self._msg.subject = subject
        print("subject added")
    
    def add_receiver(self, receiver: str):
        self._msg.receiver = receiver
        print("receiver added")

    def add_cc(self, cc: str):
        self._msg.cc = cc
        print("cc added")
        
    def add_attachement(self, path: str):
        self._msg.attachement = path
        print("Attachement added")

    @property
    def msg(self):
        msg = self._msg
        self._msg = EmailMessage()
        return msg
    ...

class EmailDirector:
    def minimalEmail(self, builder) -> None:
        self._builder = builder
        builder.add_subject("test")
        builder.add_receiver("test")
        builder.add_text("test")

    def msg(self):
        return self._builder.msg

if __name__ == "__main__":
    d = EmailDirector()
    b = EmailBuilder()
    d.minimalEmail(b)

    #or use b for custom msg
