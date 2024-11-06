student_dict = {
    "student" : ["Nimo", "Sparrow", "Barbosa"],
    "score"   : [78, 89, 85]
}


import pandas

student_dataframe = pandas.DataFrame(student_dict)
print(student_dataframe)


for (index, row) in student_dataframe.iterrows():
    print(index)
    print(row)
    print(row.student)
    if row.student == "Sparrow":
        print(row.score)