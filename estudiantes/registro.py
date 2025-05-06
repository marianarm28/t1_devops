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

def mostrar_estudiantes(estudiantes):
    # Ordenar estudiantes alfabéticamente
    estudiantes_ordenados = sorted(estudiantes, key=lambda x: x['nombre'])
    
    # Imprimir tabla
    print("-" * 30)
    print(f"{'Nombre':<20} | {'Nota':>5}")
    print("-" * 30)
    for estudiante in estudiantes_ordenados:
        print(f"{estudiante['nombre']:<20} | {estudiante['nota']:5.2f}")
    print("-" * 30)