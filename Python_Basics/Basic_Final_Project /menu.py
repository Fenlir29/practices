from actions import (
    add_student,
    view_all_students,
    view_top3,
    view_overall_average,
    view_failing_students,
    delete_student
)
from data import export_data, import_data

def get_valid_menu_option():
    while True:
        try:
            option = int(input("\nIngrese su opcion: "))
            if option >= 1 and option <= 9:
                return option
            else:
                print("Opcion invalida escoja entre el 1 y el 9 ")
        except ValueError:
            print("Entrada invalida ingrese numero")



def show_menu():
    while True:
        print("\n" + "-" * 30)
        print("MENU")
        print("-" * 30)
        print("1. Añadir alumno")
        print("2. Ver todos los alumnos")
        print("3. Ver los 3 mejores alumnos")
        print("4. Ver la nota media general")
        print("5. Ver alumnos suspendidos")
        print("6. Eliminar alumno")
        print("7. Exportar datos a CSV")
        print("8. Importar datos desde CSV")
        print("9. Salir")
        print("-" * 30)

        option = get_valid_menu_option()


        if option == 1:
            add_student()
        elif option == 2:
            view_all_students()
        elif option == 3:
            view_top3()
        elif option == 4:
            view_overall_average()
        elif option == 5:
            view_failing_students()
        elif option == 6:
            delete_student()
        elif option == 7:
            export_data()
        elif option == 8:
            import_data()
        elif option == 9:
            print("\nGracias por utilizar el Sistema de Gestión de Estudiantes. Hasta pronto.")
            return


show_menu()