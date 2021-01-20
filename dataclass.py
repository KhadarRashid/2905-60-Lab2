#immportng the dataclass 
from dataclasses import dataclass

#initializng all the variables and assigning them their types
@dataclass
class Student:
    name: str
    class_id: int
    gpa: int

    def __str__(self):(
        #returning what gets put into the variables from the main() using the __str__ function()
        return f'NAME: {self.name}, ID: {self.class_id}, GPA: {self.gpa}'

    # Main function to handle the 
def main():
    jackie = Student('Jackie', 1234, 3.9)
    print(jackie.name)
    print(jackie)
    john = Student('John', 63739, 4.0)
    print(john)

main()