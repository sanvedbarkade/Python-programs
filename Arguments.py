#types of function Arguments

''' 1 : positional arguments
2 : keyword arguments
3 : Default argument
4 : Variable number of arguments'''

def Information(Name, Age, Salary):
    print("Name is : ",Name)
    print("Age is : ",Age)
    print("Salary is : ",Salary)


Information("Amit",32,90000)

Information("Pooja",29,70000)

Information(Age = 31, Salary = 78000, Name = "Sagar")