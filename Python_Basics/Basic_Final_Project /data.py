import csv
from actions import is_valid_name, is_valid_section, is_valid_grade


def export_data(students):

    if not students:
        print("Informacion no exportada")
        return

    filename = "students.csv"
    
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['name', 'section', 'spanish', 'english', 'social_studies', 'science']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for student in students:
                writer.writerow(student)
        
        print(f"Informacion exportada a:'{filename}'")
        print(f"Estudiantes exportados: {len(students)}")
    
    except Exception as error:
        print(f"Error al expotar {error}")


def import_data(students):
    filename = "students.csv"
    
    try:
        
        with open(filename, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            
            imported_count = 0
            error_count = 0
            
            for row in reader:
                name = row.get('name', '').strip()
                section = row.get('section', '').strip().upper()
                
                try:
                    spanish = float(row.get('spanish', 0))
                    english = float(row.get('english', 0))
                    social = float(row.get('social_studies', 0))
                    science = float(row.get('science', 0))
                except ValueError:
                    error_count += 1
                    continue
                
                
                if not is_valid_name(name):
                    error_count += 1
                    continue
                
                if not is_valid_section(section):
                    error_count += 1
                    continue
                
                if not all(is_valid_grade(grade) for grade in [spanish, english, social, science]):
                    error_count += 1
                    continue
                
                
                if any(s['name'].lower() == name.lower() and 
                       s['section'] == section for s in students):
                    error_count += 1
                    continue
                
                
                student = {
                    'name': name,
                    'section': section,
                    'spanish': spanish,
                    'english': english,
                    'social_studies': social,
                    'science': science
                }
                
                students.append(student)
                imported_count += 1
            
            print(f"Importación completada")
            print(f"Se ha importado correctamente:: {imported_count} students")
            if error_count > 0:
                print(f"Se han omitido: {error_count} registros (datos no válidos o duplicados)")
            
            if imported_count == 0:
                print("No se han importado alumnos válidos.")
    
    except FileNotFoundError:
        print("No se han encontrado datos exportados anteriormente. Por favor, exporta los datos primero.")
    
    except Exception as error:
        print(f"Error al importar: {error}")