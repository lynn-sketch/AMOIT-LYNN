# CREATING CLASS CALLED STUDENTS
class Student:
    def __init__(self,name:str,reg_no:str,access_number:str,sex:str,payment:int):
        
        
        # Creating instance attributes
        self.name = name
        self.reg_no = reg_no
        self.access_number = access_number
        self.sex = sex
        self.payment = payment
        
    # Creating a method
    def information(self):
        print(f"Name:{self.name}")
        print(f"reg_no:{self.reg_no}")
        print(f"access_no:{self.access_number}")
        print(f"Sex:{self.sex}")
        # self.payment()
        # print(f"payment:{self.payment}")
        
    # creating another method for payments
    def payments(self):
        if self.payment > 1000000:
            print("fully paid")
        elif self.payment < 500000:
            print("partiaL payment")
        else:
            print("dont qualify")
            

    
Student1 = Student('Lynn','M23b23','f23','female',2000000)
            
Student1.information()
Student1.payments()           
    
        
        