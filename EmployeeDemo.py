import datetime
import os


class Employee:
    def __init__(self, emp_name, emp_id):
        self.__emp_name = emp_name
        self.__emp_id = emp_id

    def set_name(self, emp_name):
        self.__emp_name = emp_name

    def set_id(self, emp_id):
        self.__emp_id = emp_id

    def get_name(self):
        return self.__emp_name

    def get_id(self):
        return self.__emp_id


class ProductionWorker(Employee):
    def __init__(self, emp_name, emp_id, shift, pay_rate):
        super().__init__(emp_name, emp_id)
        self.__shift = shift
        self.__pay_rate = pay_rate

    def set_shift(self, shift):
        self.__shift = shift

    def set_pay_rate(self, pay_rate):
        self.__pay_rate = pay_rate

    def get_shift(self):
        return self.__shift

    def get_pay_rate(self):
        return self.__pay_rate


class ShiftSupervisor(Employee):
    def __init__(self, emp_name, emp_id, salary, bonus):
        super().__init__(emp_name, emp_id)
        self.__salary = salary
        self.__bonus = bonus

    def set_salary(self, salary):
        self.__salary = salary

    def set_bonus(self, bonus):
        self.__bonus = bonus

    def get_salary(self):
        return self.__salary

    def get_bonus(self):
        return self.__bonus


# print date time path and lab
x = datetime.datetime.now()
print(os.environ['PYTHONPATH'])
print('Programmer:' + os.getlogin())
print('Lab 19.3', x.strftime('%B %d, %Y @ %I:%M:%S\n'))


def main():
    # Get all of the user inputs and store them in variables
    name = input("Enter your name: ")
    employee = input("Enter the employee's name: ")
    employee_id = eval(input("Enter the ID number: "))
    salary = eval(input("Enter the shift number: "))
    bonus = eval(input("Enter the hourly pay rate: "))

    print(f"{name}, here is the Shift supervisor, {employee}'s information:\n")

    sup = ShiftSupervisor(employee, employee_id, salary, bonus)

    print(f"Name: {sup.get_name()}")
    print(f"ID number: {sup.get_id()}")
    print(f"Annual Salary: ${sup.get_salary():,.2f}")
    print(f"Annual Production Bonus: ${sup.get_bonus():,.2f}")


main()
