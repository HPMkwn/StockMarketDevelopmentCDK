from datetime import date

class BaseModel(type):

    def __new__(cls, name, bases, attrs):
        if name == 'BaseModel':
            return type.__new__(cls, name, bases, attrs)
        print(">>", name)
        return type.__new__(cls, name, bases, attrs)    
    
    def __init__(self, id: str, updatedAt : date):  
        self.id = id
        self.updatedAt = updatedAt