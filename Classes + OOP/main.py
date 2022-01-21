class People:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary
class Employee(People):

    def __init__(self,name,salary, age):

        super().__init__(name)

        self.age = age

        

    def isEmployee(self):

        return True
def main():
  p = People("Duy", 1000)
  em=Employee("Duy", 1000, 22)
  print(f"{em}. My age: {em.age}")
if __name__ == '__main__':
    main()
