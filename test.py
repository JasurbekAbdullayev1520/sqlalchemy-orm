from datetime import date
from school.create_tables import init_db
from school.crud import (
    create_student,
    get_students,
    get_one_student,
    search_students_by_first_name,
    search_students_by_name,
    update_student,
    filter_students_by_gender,
    filter_students_by_gpa,
    get_sorted_students_by_gpa,
    add_score,
    get_scores,
    get_student_with_scores,
)

init_db()


# create_student('ali', 'valiyev3', date(2005, 9, 3))

# students = get_students()
# print(students)

# s = get_one_student(1)
# print(s.bio)

# sts = search_students_by_first_name('ali')
# print(sts)

# sts = search_students_by_name('vali')
# print(sts)

# update_student(1, last_name='nimadir')


# females = filter_students_by_gender('Female')
# for female in females:
#     print(female.gender, female.full_name)

# sts = filter_students_by_gpa(3, 3.1)
# for s in sts:
#     print(s.gpa, s.first_name)


# sts = get_sorted_students_by_gpa('desc')
# for s in sts:
#     print(s.gpa, s.first_name)


# add_score(88, 'english', 4)
# print(get_scores(87))

print(get_student_with_scores()[86:88])


