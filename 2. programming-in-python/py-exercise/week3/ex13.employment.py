class Employee:
    def __init__(self, name, last) -> None:
        self.name = name
        self.last = last

class Supervisors(Employee):
    def __init__(self, name, last, password) -> None:
        super().__init__(name, last)
        self.password = password

class Chefs(Employee):
    def leave_request(self, days):
        return "May I take a lieave for " + str(days) + " days"

#supervisor info
a = Supervisors("Adrian", "A", "1234")
print(a.password, a.name, a.last)

#chef info
b = Chefs("Emily", "B")
print(b.leave_request(5))
print(b.name, b.last)
