"""

employee = {
    "name" : "Daniel",
    "age" : "32",                                       # " KEY(STRING): VALUE(DYNAMIC)
    "salary" : "45,000 $",                              # Key:value = pair data
}

print(employee["name"])
print(employee["age"])
print(employee["salary"])


#keys()

print(employee.keys())
print(employee.values())

#update()

employee.update({"age":30})
print(employee)


employee.pop("age")
print(employee)

"""

#Dictionary to JSON Str



"""
import json


employee_string = {
    "name" : "Daniel",
    "age" : "32",
"salary" : "45,000 $",
}

employee_string = json.dumps(employee_string)
print(employee_string)

"""
#JSON string to Dictionary
"""
import json

employee_string =  '{"name": "Daniel", "age": "32", "salary": "45,000 $"}'
employee_dict = json.loads(employee_string)
print(employee_dict)
"""


