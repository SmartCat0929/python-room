name = input("name:")
age = input("nage:")
job = input("job:")
salary = input("salary:")
msg = '''
--------info of %s---------
name: %s  
age: %d
job: %s
salary: %d
---------end----------
''' % (name, name, age, job, salary)
print(msg)
