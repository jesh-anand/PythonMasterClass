class Employee:
    def __init__(self, first, last, sex):
        self.first = first
        self.last = last
        self.sex = sex
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return "{} {}".format(self.first, self.last)


def main():
    emp_1 = Employee('prajesh', 'ananthan', 'male')
    print(emp_1.fullname())


if __name__ == '__main__':
    main()
