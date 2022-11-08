from roster import student_roster
import itertools

class ClassroomOrganizer:
  def __init__(self):
    self.sorted_names = self._sort_alphabetically(student_roster)

  def __iter__(self):
    self.index = 0
    return self 

  def __next__(self):
    if self.index < len(self.sorted_names):
        student = self.sorted_names
        self.index +=1
        return student
    else:
        raise StopIteration


  def _sort_alphabetically(self,students):
    names = []
    for student_info in students:
      name = student_info['name']
      names.append(name)
    return sorted(names)


  def get_students_with_subject(self,subject):
    selected_students = []
    for student in student_roster:
      if student['favorite_subject'] == subject:
        selected_students.append((student['name'], subject))
    return selected_students


  def seat_combination(self):
    self.students = self._sort_alphabetically(student_roster)
    student_combination = list(itertools.combinations(self.students,2))
    return student_combination
  
