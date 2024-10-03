import random

#These are the grades I got for the first two years

first_year_grade = 0.499
second_year_grade = 0.5589

#These are dictionaries that hold the modules, their weights and the final grades
Modules = ["Comprehensives", "ACP", "FQM", "Astrophysics", "Essay", "SSP", "NPP", "Hydro"]
Weights = {"Comprehensives":15.0, "ACP":7.5, "FQM": 7.5, "Astrophysics": 7.5, "Essay": 7.5, "SSP": 5.0, "NPP": 5.0, "Hydro": 5.0}
Grades = {"Comprehensives":0.792, "ACP":0.8, "FQM": 0.9, "Astrophysics": 0.8, "Essay": 0.75, "SSP": 0.75, "NPP": 0.85, "Hydro": 0.9}

def final_year_append(Name, Grade):
  #This function allows you to change the final grade manually
  Grades[Name] = Grade
  return print(Grades[Name])

def final_year_grade():
  #This function allows you to calculate the final year grade
  results = []
  for i in Modules:
    results.append(Weights[i]*Grades[i])
  return sum(results) / 60.0

def lowest_grade():
  #This selects the first module in a shuffled list of modules and manually decreases its value until the final grade
  #drops bellow 70%, at which point it displays the final grade, final-year grades, and module grades 
  lowest_grades = []
  final_grade = 1
  random.shuffle(Modules)
  for i in Modules:
    while True:
      if final_grade > 0.7:
        Grades[i] -= 0.005
        third_year_grade = final_year_grade()
        final_grade = ((first_year_grade * 7.5) + (second_year_grade * 35.0) + (third_year_grade * 57.5)) / 100.0
      else:
        lowest_grades.append(f"{i}: {Grades[i]}")
        break
  return lowest_grades, third_year_grade, final_grade

def predictor():
  #This function repeats the lowest_grade function a set number of times, to give you an idea of what kind of grades you need to succeed!
  Predictions = []
  Grades = []
  for i in range(20):
    Predictions.append(lowest_grade())
  return Predictions