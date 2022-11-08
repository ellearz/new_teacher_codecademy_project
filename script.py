from roster import student_roster
from classroom_organizer import ClassroomOrganizer
import itertools

iter_student_roster = iter(student_roster)
for student in iter_student_roster:
    print(student)

classroomorganizer = ClassroomOrganizer()
classroomorganizer_iter = classroomorganizer
for student in classroomorganizer:
    print(student)

students_seats =ClassroomOrganizer.seat_combination(classroomorganizer)
for seat in students_seats:
    print(seat)



math_science_fav_students= itertools.chain(classroomorganizer.get_students_with_subject("Math"),classroomorganizer.get_students_with_subject("Science"))

for m in math_science_fav_students:
    print(m)

comb_of_four_students_fav = list(itertools.combinations(math_science_fav_students,4))
print(comb_of_four_students_fav)
    