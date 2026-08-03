from student import Student

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

def student_exists(students, name, section):
    for student in students:
        if (student.name.lower() == name.lower() and
            student.section.upper() == section.upper()):
            return True

    return False

def add_student(students):
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
    
    if student_exists(students,name,section):
        print(f"\nEstudiante {name} ya estaba en el sistema en la {section}")

        return

    print("Ingrese las notas (0-100): ")
    spanish = get_valid_grade("spanish")
    english = get_valid_grade("english")
    social = get_valid_grade("social")
    science = get_valid_grade("science")


    student = Student(name, section, spanish, english, social, science)
    students.append(student)


    print(f"Estudiante '{name}' se agrego exitosamente")
def calculate_student_average(student):
    return student.calculate_average()

def view_all_students(students):
    if not students:
        print("No hay estudiantes en el sistema")
        return

    print(f"{'name':<25} {'section':<10} {'spanish':<8} {'english':<8} {'social':<8} {'science':<8} {'Media':<8}")
    print("-" * 75)

    for student in students:
        avg = student.calculate_average()
        print(f"{student.name:<25} {student.section:<10} "
              f"{student.spanish:<8.1f} {student.english:<8.1f} "
              f"{student.social:<8.1f} {student.science:<8.1f} "
              f"{avg:<8.1f}")

def view_top3(students):
    
    if not students:
        print("No hay estudiantes en el sistema.")
        return
    
    sorted_students = sorted(
    students,
    key=calculate_student_average,
    reverse=True
)
    
    # error si solo hay 2 o menos estudiantes 
    top_count = min(3, len(sorted_students))

    print(f"\n{'Clasificación':<6} {'name':<15} {'section':<10} {'Media':<8}")
    print("-" * 50)

    for i in range(top_count):
        student = sorted_students[i]
        avg = student.calculate_average()
        print(f"{i+1:<6} {student.name:<25} {student.section:<10} {avg:<8.1f}")

def view_overall_average(students):

    if not students:
        print("No hay estudiantes en el sistema.")
        return

    total_sum = 0
    total_count = 0

    for student in students:
        total_sum += student.calculate_average()
        total_count += 1

    overall_avg = total_sum / total_count
    print(f"Media general de todos los alumnos: {overall_avg:.2f}")

def view_failing_students(students):
    if not students:
        print("No hay estudiantes en el sistema.")
        return

    failing_students = []
    
    for student in students:
        failing_subjects = student.get_failing_subjects()
        
        if failing_subjects:
            failing_students.append({
                'estudiante': student,
                'asignaturas_suspendidas': failing_subjects 
            })
    
    if not failing_students:
        print("No hay estudiantes reprobados")
        return

    print(f"\n{'Nombre':<25} {'Sección':<10} {'Asignaturas suspendidas'}")
  
    for entry in failing_students:
        student = entry['estudiante']
        subjects_str = ", ".join([f"{subj}: {grade:.1f}" 
                                 for subj, grade in entry['asignaturas_suspendidas']])
        print(f"{student.name:<25} {student.section:<10} {subjects_str}")

def delete_student(students):

    if not students:
        print("No hay estudiantes en el sistema.")
        return

    name = input("Ingrese el nombre completo: ").strip()
    section = input("Ingrese la section: ").strip().upper()

    student_to_delete = None
    for student in students:
        if student.name.lower() == name.lower() and student.section == section:
            student_to_delete = student
            break

    if not student_to_delete:
        print(f"Estudiante '{name}' de la seccion {section} no se encontro en el sistema")
        return

    
    print(f"\nEstudiante encontrado:")
    print(f"Nombre: {student_to_delete.name}")
    print(f"Sección: {student_to_delete.section}")
    print(f"Media: {student_to_delete.calculate_average():.1f}")

    confirm = input(f"\nSeguro que quieres eliminar este estudiante? (y/n): ")
    if confirm.lower() == 'y':
        students.remove(student_to_delete)
        print(f"\nEstudiante '{name}' eliminado del sistema")
    else:
        print("\nEliminacion cancelada.")

