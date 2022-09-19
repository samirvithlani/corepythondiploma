employees = ("John", "Mary", "Peter", "Susan", "John")
print(employees)

for emp in employees:
    print(emp)

print("0th index",employees[0])    

cnt = employees.count("John")
print("John count",cnt)

x = employees.index("Peter")
print(x)