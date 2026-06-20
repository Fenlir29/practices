total_passing_notes = 0
average_passing = 0
total_average_score = 0
total_failing_grade = 0
average_fail = 0

print("cuantas notas quieres procesar ?")
total_grade = int(input())


for i in range(total_grade):
    Current_note = int(input("ingrese nota:"))
    if Current_note < 70:
        total_failing_grade = total_failing_grade +1
        average_fail = average_fail + Current_note
    else:
        total_passing_notes = total_passing_notes + 1
        average_passing = average_passing + Current_note
    total_average_score += Current_note / total_grade

if total_passing_notes > 0:
    average_passing = average_passing / total_passing_notes   
else:
    average_passing = 0

if total_failing_grade > 0:
    average_fail = average_fail / total_failing_grade  
else:
    average_fail = 0



print(f"El total de notas aprobadas es:{total_passing_notes}")
print(f"El promedio de notas aprobadas es:{average_passing:.2f}")
print(f"El total de notas desaprobadas es:{total_failing_grade}")
print(f"El promedio de notas desaprobadas es:{average_fail:.2f}")
print(f"El Promedio total de notas es:{total_average_score:.2f}")



