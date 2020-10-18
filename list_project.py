last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
print(subjects)
print(grades)

subjects.append("computer science")
grades.append(100)

gradebook = list(zip(subjects, grades))
gradebook.append(("visual arts", 93))
print(gradebook)

full_gradebook = gradebook + last_semester_gradebook
print(full_gradebook)
range_cap = len(full_gradebook)
gradebook_range = range(range_cap)

def letter_grade(grade):
  if grade >= 90:
    return "Passed with an 'A'"
  elif grade >= 80:
    return "Passed with a 'B'"
  elif grade >= 70:
    return "Passed with a 'C'"
  elif grade >= 60:
    return "Passed with 'D', but no credit earned."
  else:
    return "Failed class with 'F', no credits earned."
for grade in full_gradebook:
  print("Class: "+str(grade[0]))
  print("Grade: "+str(grade[1]))
  print(letter_grade(grade[1]))
  
