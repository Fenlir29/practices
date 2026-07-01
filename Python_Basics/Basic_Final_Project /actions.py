students = []
def is_valid_name(name):
    if not name or not name.strip():
        return False
    
    for char in name:

        if not char.isalpha() and not char.isspace():
            return False

    return True

#buscar como hacer validacion de formato (11B)
def is_valid_section(section):
    if not section or not section.strip():
        return False
    else:
        return True

def is_valid_grade(grade):
    try:
        grade_value = float(grade)

        if grade_value < 0 or grade_value > 100:
            return False

        return True

    except (ValueError, TypeError):
        return False

def get_valid_grade(subject):
    while True:
        grade = float(input(f"ingrese la nota de {subject}: "))
        if is_valid_grade(grade):
            return grade
        else:
            print("nota invalida intente otra vez")

def student_exists(name, section):
    for student in students:
        if (student["nombre"].lower() == name.lower() and
            student["seccion"].upper() == section.upper()):
            return True

    return False

def add_student():
    while True:
        name = input("ingrese el nombre completo: ").strip()
        if is_valid_name(name):
            break
        else:
            print("nombre invalido intente otra vez")

    while True:
        section = input("Ingrese la seccion (10A)").strip().upper()
        if is_valid_section(section):
            break
        else:
            print("Seccion invalida intente otra vez")
    
    if student_exists(name,section):
        print(f"\nEstudiante {name} ya estaba en el sistema en la {section}")

        return

    print("Ingrese las notas (0-100): ")
    spanish = get_valid_grade("Español")
    english = get_valid_grade("Ingles")
    social = get_valid_grade("sociales")
    science = get_valid_grade("Ciencias")

    student = {
        'nombre': name,
        'seccion': section,
        'español': spanish,
        'ingles': english,
        'sociales': social,
        'ciencias': science
    }

    students.append(student)
    print(f"Estudiante '{name}' se agrego exitosamente")

def calculate_student_average(student):
    return (student['español'] + student['ingles'] + 
            student['sociales'] + student['ciencias']) / 4

def view_all_students():
    if not students:
        print("No hay estudiantes en el sistema")
        return

    print(f"{'nombre':<25} {'seccion':<10} {'español':<8} {'ingles':<8} {'sociales':<8} {'ciencias':<8} {'Media':<8}")
    print("-" * 75)

    for student in students:
        avg = calculate_student_average(student)
        print(f"{student['nombre']:<25} {student['seccion']:<10} "
              f"{student['español']:<8.1f} {student['ingles']:<8.1f} "
              f"{student['sociales']:<8.1f} {student['ciencias']:<8.1f} "
              f"{avg:<8.1f}")

def view_top3():
    
    if not students:
        print("No hay estudiantes en el sistema.")
        return
    
    sorted_students = sorted(students, 
                           key=calculate_student_average, 
                           reverse=True)
    
    # error si solo hay 2 o menos estudiantes 
    top_count = min(3, len(sorted_students))

    print(f"\n{'Clasificación':<6} {'nombre':<15} {'seccion':<10} {'Media':<8}")
    print("-" * 50)

    for i in range(top_count):
        student = sorted_students[i]
        avg = calculate_student_average(student)
        print(f"{i+1:<6} {student['nombre']:<25} {student['seccion']:<10} {avg:<8.1f}")

def view_overall_average():

    if not students:
        print("No hay estudiantes en el sistema.")
        return

    total_sum = 0
    total_count = 0

    for student in students:
        total_sum += calculate_student_average(student)
        total_count += 1

    overall_avg = total_sum / total_count
    print(f"Media general de todos los alumnos: {overall_avg:.2f}")

def view_failing_students():

    failing_students = []
    
    for student in students:
        failing_subjects = []
        
        if student['español'] < 60:
            failing_subjects.append(('español', student['español']))
        if student['ingles'] < 60:
            failing_subjects.append(('ingles', student['ingles']))
        if student['sociales'] < 60:
            failing_subjects.append(('sociales', student['sociales']))
        if student['ciencias'] < 60:
            failing_subjects.append(('ciencias', student['ciencias']))
        
        if failing_subjects:
            failing_students.append({
                'estudiante': student,
                'asignaturas suspendidas': failing_subjects
            })
    if not failing_students:
        print("No hay estudiantes reprobados")
        return

    print(f"\n{'nombre':<25} {'seccion':<10} {'asignaturas suspendidas'}")

    for entry in failing_students:
        student = entry['estudiante']
        subjects_str = ", ".join([f"{subj}: {grade:.1f}" 
                                 for subj, grade in entry['asignaturas suspendidas']])
        print(f"{student['nombre']:<25} {student['seccion']:<10} {subjects_str}")

def delete_student():

    if not students:
        print("No hay estudiantes en el sistema.")
        return

    name = input("Ingrese el nombre completo: ").strip()
    section = input("Ingrese la seccion: ").strip().upper()

    student_to_delete = None
    for student in students:
        if student['nombre'].lower() == name.lower() and student['seccion'] == section:
            student_to_delete = student
            break

    if not student_to_delete:
        print(f"Estudiante '{name}' de la seccion {section} no se encontro en el sistema")
        return

    
    print(f"\nEstudiante encontrado:")
    print(f"nombre: {student_to_delete['nombre']}")
    print(f"seccion: {student_to_delete['seccion']}")
    print(f"media: {calculate_student_average(student_to_delete):.1f}")

    confirm = input(f"\nSeguro que quieres eliminar este estudiante? (y/n): ")
    if confirm.lower() == 'y':
        students.remove(student_to_delete)
        print(f"\nEstudiante '{name}' eliminado del sistema")
    else:
        print("\nEliminacion cancelada.")

