'''
A wise man said "the decorator pattern is a means to add functionality to an object at runtime."
so individual object gets the modified behavior.

it adds functionality to existing object

like text tags bold, italic we add functionality to only that part of font

suppose we want to notify a user when an action happens 
we can use mobile sms email fb_msg
but this diffrs from user to another and event to another
for ex. for important events we will use all of them
for unimportant events we may use fb only
and so on ...


or auth system for backends
'''


# class Notifier:
#     def notify(self):
#         return "user Default notification for fb"

# class SMSNotifier(Notifier):
#     def __init__(self, usernotification) -> None:
#         self.un = usernotification

#     def notify(self):
#         return f"User notified by sms along with {self.un.notify()}"

# class EmailNotifier(SMSNotifier):
#     def notify(self):
#         return f"User notified by email along with {self.un.notify()}"

class BasicAuth:
    def auth(self):
        return "User Authorized"

class DecoratorAuth(BasicAuth):
    def __init__(self, auth) -> None:
        self.b_a = auth
    

class LoggedIn(DecoratorAuth):
    def auth(self):
        return f"User logged in, and {self.b_a.auth()}"

class HaveSpecialPerm(DecoratorAuth):
    def auth(self):
        return f"User have Special Perm, and {self.b_a.auth()}"

if __name__ == '__main__':
    a = BasicAuth()
    print(a.auth())

    # now for important perm

    i_a = HaveSpecialPerm(LoggedIn(a))

    print(i_a.auth())