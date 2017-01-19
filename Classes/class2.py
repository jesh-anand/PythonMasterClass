class Employee:
    # global variables
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


def main():
    emp_1 = Employee('prajesh', 'ananthan', 10000)
    emp_2 = Employee('sasha', 'ananthan', 5000)
    print(Employee.num_of_emps)


if __name__ == '__main__':
    main()
