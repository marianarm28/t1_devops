import csv

def cargar_estudiantes(archivo_csv):
    estudiantes = []
    with open(archivo_csv, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for fila in reader:
            try:
                nota = float(fila['nota'])
                if 0.0 <= nota <= 5.0:
                    estudiantes.append({
                        'nombre': fila['nombre'],
                        'nota': nota
                    })
                else:
                    print(f"Advertencia: Nota fuera de rango para {fila['nombre']}")
            except ValueError:
                print(f"Advertencia: Nota inválida para {fila['nombre']}")
    return estudiantes