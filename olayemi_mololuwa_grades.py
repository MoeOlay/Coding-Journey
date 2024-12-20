grades_list = [83,85,72,65,76,90,79,88,93,70,67,80]
attendance_set_1 = {'Mary','Jake','Sam','Alex','Percy','Jessica','Trent','Mahmoud'}
attendance_set_2 = {'Jake','Sam','Alex','Percy','Mahmoud','Trent','Caleb','Zayne'}
exams_taken = len(grades_list)
low_grade = min(grades_list)
high_grade = max(grades_list)
avg_grade = sum(grades_list)/len(grades_list)
print(f'{exams_taken} Students took the exam.\nThe highest grade was a {high_grade}\nThe lowest grade was a {low_grade}\nThe average grade for the exam was a {avg_grade}')

students_attended = len(attendance_set_1.union(attendance_set_2))
attended_both =attendance_set_1.intersection(attendance_set_2) 
attended_one = (attendance_set_1.difference(attendance_set_2)).union(attendance_set_2.difference(attendance_set_1))
print(f'\n{students_attended} students attended the class.\n{attended_both} attended both class days.\n{attended_one} attended one class day.')