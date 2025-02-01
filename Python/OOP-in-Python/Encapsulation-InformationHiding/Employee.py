class Employee:
    def __init__(self, name="", ID=0, department=""):
        self.__name = name
        self.__ID = ID
        self.__department = department
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_ID(self):
        return self.__ID

    def set_ID(self, ID):
        self.__ID = ID

    def get_department(self):
        return self.__department

    def set_department(self, department):
        self.__department = department

