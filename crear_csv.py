import pandas as pd

# Definir los datos como un diccionario
data = {
    "price": [5000, 7000, 12000],
    "year": [2012, 2015, 2018],
    "manufacturer": ["ford", "toyota", "honda"],
    "model": ["focus", "corolla", "civic"],
    "condition": ["good", "excellent", "like new"],
    "cylinders": [4, 4, 4],
    "fuel": ["gas", "gas", "gas"],
    "odometer": [120000, 80000, 50000],
    "title_status": ["clean", "clean", "clean"],
    "transmission": ["automatic", "automatic", "automatic"],
    "drive": ["fwd", "fwd", "fwd"],
    "size": ["compact", "compact", "compact"],
    "type": ["sedan", "sedan", "sedan"],
    "paint_color": ["blue", "black", "white"],
    "state": ["ca", "ny", "tx"],
    "posting_date": ["2023-01-01", "2023-02-15", "2023-03-10"]
}

# Convertir el diccionario en un DataFrame
df = pd.DataFrame(data)

# Guardar el DataFrame como un archivo CSV
df.to_csv("vehicles_us.csv", index=False)

print("✅ Archivo 'vehicles_us.csv' creado con éxito!")
