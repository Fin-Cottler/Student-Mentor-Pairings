from Levenshtein import ratio
from student import Student
from mentor import Mentor
from termcolor import colored

class Matrix:
    all_matrices = []
    all_matches = []

    def __init__(self, student, mentor, result):
        self.result = result
        self.student = student
        self.mentor = mentor
        Matrix.all_matrices.append(self)

    @classmethod
    def create_matrices(cls):

        Mentor.instantiate_from_csv_mentor("Data/advisor.csv")
        Student.instantiate_from_csv_student("Data/student.csv")

        for student in Student.all_students:
            for mentor in Mentor.all_mentors:

                interest1_list = []
                interest2_list = []
                interest3_list = []

                substr_len1 = 1
                substr_len2 = 1
                substr_len3 = 1

                interest1_res = 0
                interest2_res = 0
                interest3_res = 0
                

                for char in student.interest1:
                    interest1_list.append(ratio(student.interest1[0:substr_len1],mentor.interest1[0:substr_len1]))
                    substr_len1 += 1

                interest1_list.sort(reverse=True)
                interest1_res = interest1_list[0]
                interest1_list.clear()
                
                for char in student.interest2:
                    interest2_list.append(ratio(student.interest2[0:substr_len2],mentor.interest1[0:substr_len2]))
                    substr_len2 += 1

                interest2_list.sort(reverse=True)
                interest2_res = interest2_list[0]
                interest2_list.clear()

                for char in student.interest3:
                    interest3_list.append(ratio(student.interest3[0:substr_len3],mentor.interest3[0:substr_len3]))
                    substr_len3 += 1

                interest3_list.sort(reverse=True)
                interest3_res = interest3_list[0]
                interest3_list.clear()

                final_result = (interest1_res + interest2_res + interest3_res)/3

                Matrix(
                    student = student,
                    mentor = mentor,
                    result = final_result
                )
        Matrix.all_matrices.sort(key = Matrix.get_result, reverse=True)

    def __repr__(self):
        return f"[{self.student.name}],[{self.mentor.name}],[{self.result}]"
    
    def get_result(self):
        return self.result
      
    def __hash__(self):
        return hash((self.student,self.mentor)) 
  
    def __eq__(self,other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return (isinstance(other, type(self))
            and (self.student, self.mentor) ==
          (other.student, other.mentor))
    
    @classmethod
    def print_matrices(cls):
        count = 0
        stop_count = 0
        if(len(Matrix.all_matrices) > 0):
            for matrix in Matrix.all_matrices:
                if stop_count == 100:
                    break
                print(matrix)
                stop_count += 1
            for matrix in Matrix.all_matrices:
                count += 1
        else:
            print("Nothing in list")
        print("...")
        print(colored(f"{count} in list", color="green"))


    @classmethod
    def match(cls):
        match_list = []
        count = 0
        for matrix in Matrix.all_matrices:
            if(
                len(matrix.mentor.student_list) < matrix.mentor.slots_avail and
                len(Matrix.all_matrices) > 0 and
                matrix.student not in match_list
               ):
                matrix.mentor.student_list.append(matrix.student)
                print(f"{matrix.student.name} was matched with {matrix.mentor}. sim: {matrix.result * 100}")
                match_list.append(matrix.student)
                Matrix.all_matches.append(matrix)
                count += 1

            elif len(Matrix.all_matrices) > 0:
                pass

            else:
                break
        print(colored(f"{count} matches","yellow"))
        
        

        
    
