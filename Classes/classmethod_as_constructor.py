'''Using classmethod as constructor to a class'''
class Employee:
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


def main():
    emp_str_1 = 'prajesh-ananthan-10000'
    emp1_new = Employee.from_string(emp_str_1)
    print(emp1_new.email)


if __name__ == '__main__':
    main()
