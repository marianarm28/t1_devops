from estudiantes.registro import cargar_estudiantes, mostrar_estudiantes, calcular_promedio

def main():
    estudiantes = cargar_estudiantes('estudiantes.csv')
    mostrar_estudiantes(estudiantes)
    promedio = calcular_promedio(estudiantes)
    print(f"Promedio general: {promedio:.2f}")

if __name__ == "__main__":
    main()