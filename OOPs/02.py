
class bio:
    def __init__(self , name , working):
        self.name = name
        self.working = working
    def data_returning(self):
        return f"Name : {self.name} , Working : {self.working}"

my_class = bio('python classes' , 'working on oops')

# print(my_class.data_returning())

    
    
    
    
    
    
    
class Counts:
    def __init__(self , a , b):
        self.a = a
        self.b = b
        # print(a + b)
    
    def addition(self):
        return self.a + self.b
    def subtraction(self):
        return self.a - self.b
    def divide(self):
        return self.a / self.b
    def multiplacation(self):
        return self.a * self.b


data_view = Counts(2 , 4)
# print(data_view.divide())

# Inheritance


class MyApp:
    def __init__(self, user_name , user_pass ):
        self.user_name = user_name
        self.user_pass = user_pass
    
    def is_user_loggin(self):
        return True
    
    def showing_user_credentials(self):
        user_cred = {
            "user_name" : self.user_name,
            "user_pass" : self.user_pass
        }
        return user_cred

user1 = MyApp('a' , '123')
user2 = MyApp('b' , '456')

class Chat():
    def __init__(self , sender , reciever , messege):
        self.sender = sender
        self.reciever = reciever
        self.messege = messege
    
    # chat box
    def chat_box(self):
        return f"""
    FROM :{self.sender}
    TO :  {self.reciever}
    Messege : {self.messege} """


my_chat_box = Chat(user1.user_name , user2.user_name , 'hello')

print(my_chat_box.chat_box())
