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

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount


def main():
    emp_1 = Employee('prajesh', 'ananthan', 10000)
    emp_2 = Employee('sasha', 'ananthan', 5000)
    Employee.set_raise_amount(1.05)
    emp_1.apply_raise()
    emp_2.apply_raise()
    print(emp_1.pay)
    print(emp_2.pay)


if __name__ == '__main__':
    main()
