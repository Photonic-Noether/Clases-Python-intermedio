import pandas as pd

def analizar_csv():
    # Cargar el archivo CSV
    df = pd.read_csv('clase01_csv.csv')
    
    # 1) Número total de personas
    total_personas = len(df)
    print(f"1) Número total de personas: {total_personas}")
    print("-" * 50)
    
    # 2) Mostrar nombre y ocupación de los 12 primeros
    print("2) Primeras 12 personas (NOMBRE - OCUPACION):")
    print("-" * 30)
    for i, (_, row) in enumerate(df.head(12).iterrows(), 1):
        print(f"{row['nombre']} - {row['ocupacion']}")
    print("-" * 50)
    
    # 3) Crear columna is_remote
    # Definir qué ocupaciones son remotas
    ocupaciones_remote = ['Ingeniero', 'Desarrollador']
    
    # Crear la nueva columna
    df['is_remote'] = df['ocupacion'].isin(ocupaciones_remote)
    
    # Mostrar algunas filas con la nueva columna
    print("3) Dataset con nueva columna 'is_remote':")
    print("-" * 60)
    print(df[['nombre', 'ocupacion', 'is_remote']].head(15))
    print("-" * 60)
    
    # Estadísticas de la nueva columna
    total_remote = df['is_remote'].sum()
    print(f"Total de personas en remoto: {total_remote}")
    print(f"Total de personas no remotas: {total_personas - total_remote}")
    
    # Guardar el resultado en un nuevo archivo (opcional)
    df.to_csv('clase01_csv_con_remote.csv', index=False)
    print(f"\nArchivo guardado como 'clase01_csv_con_remote.csv'")
    
    return df

if __name__ == "__main__":
    analizar_csv()