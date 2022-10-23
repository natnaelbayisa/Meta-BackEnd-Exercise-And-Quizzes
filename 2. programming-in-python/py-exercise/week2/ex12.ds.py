#employee list

#Instead of two employees, you may have 2000 or even 20,000.
#The code will have to iterate over the list sequentially until the number is matched. 
employee_list = [{"id":1, "Name":"A", "Department":":CS"}, {"id":2, "Name":"B", "Department":"com-eng"}]

#only works with key not value
def get_employee(id):
    for employee in employee_list:
        if employee["id"]==id:
            return employee
        
print(get_employee(1))
print(get_employee(2))


# The main difference with the below code is that you no longer need to iterate over the list to locate them.
employee_dict = {
    3:{
        "id":3,
        "Name":"C",
        "Department":"CS"
    },
    
    4:{
        "id":4,
        "Name":"D",
        "Department":"com-eng"
    },
}

def get_employee_from_dict(id):
    return employee_dict[id]

print(get_employee_from_dict(3))
print(get_employee_from_dict(4))



        