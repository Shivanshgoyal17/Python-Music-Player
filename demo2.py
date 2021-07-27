# hasattr() concept

class Student:
    def __init__(self):
        self.roll=101
        self.name="Shivansh"
        self.per=99.8

obj=Student()
print(hasattr(obj,"roll"))
print(hasattr(obj,"gender"))

# hasattr() returns true or false It is used for checking ki koi instance member kisi class ke andar hai ki ni