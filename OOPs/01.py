
class bio:
    def __init__(self , name , working):
        self.name = name
        self.working = working
    def data_returning(self):
        return f"Name : {self.name} , Working : {self.working}"

my_class = bio('python classes' , 'working on oops')

print(my_class.data_returning())
    