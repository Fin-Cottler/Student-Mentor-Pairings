import csv
class Student:
  
  all_students = []
  
  def __init__(self, name, interest1, interest2, interest3):
    self.name = name
    self.interest1 = interest1
    self.interest2 = interest2
    self.interest3 = interest3
    self.all_students.append(self)

  def __repr__(self): 
    return self.name

  @classmethod 
  def instantiate_from_csv_student(cls, filename: str):
    with open(filename, "r") as f:
      reader = csv.DictReader(f)
      mentorlist = list(reader)
    for mentor in mentorlist:
      Student(
        name=mentor['Name'],
        interest1=mentor['Interest 1'],
        interest2=mentor['Interest 2'],
        interest3=mentor['Interest 3']
      )