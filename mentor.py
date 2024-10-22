import csv
from termcolor import colored

class Mentor:
  all_mentors = []
  
  def __init__(self, name, interest1, interest2, interest3, slots_avail):
    self.name = name
    self.interest1 = interest1
    self.interest2 = interest2
    self.interest3 = interest3
    self.slots_avail = int(slots_avail)
    self.student_list = []
    self.all_mentors.append(self)

  
  def __repr__(self): 
    return f"{self.name}: {self.slots_avail}"

  def get_num(self):
    return self.slots_avail

  @classmethod
  def print_pairings(cls):
    for mentor in Mentor.all_mentors:
      print(mentor)
      print(colored(mentor.student_list, color ="red"))

  @classmethod 
  def instantiate_from_csv_mentor(cls, filename: str):
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        mentorlist = list(reader)
    for mentor in mentorlist:
        Mentor(
          name=mentor['Name'],
          interest1=mentor['Interest 1'],
          interest2=mentor['Interest 2'],
          interest3=mentor['Interest 3'],
          slots_avail=mentor['Slots Avail']
        )