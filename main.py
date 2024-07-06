from fastapi import FastAPI
import pandas as pd

app = FastAPI()

app.title = "MLOps plataforma de streaming"

#Cargo el archivo parquet
df_movies = pd.read_parquet('movies_data.parquet')

#Creo un diccionario para obtener los meses en español de acuerdo al numero
meses_español = {
    "enero": 1, "febrero": 2, "marzo": 3, "abril": 4, "mayo": 5, "junio": 6,
    "julio": 7, "agosto": 8, "septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12
}

@app.get('/cantidad_filmaciones_mes/{mes}')
async def cantidad_filmaciones_mes(mes: str):
    #Convierto el mes a minusculas para que la funcion distinga entre minusculas y mayusculas(case-insensitive)
    mes = mes.lower()

    #Verififo si el mes recibido es valido
    if mes not in meses_español:
        return f"Error: {mes} no es válido. Por favor, ingrese un mes en español."
    
#Filtro las peliculas de acuerdo al mes ingresado
    peliculas_mes = df_movies[df_movies['release_date'].dt.month == meses_español[mes]]


 #Cuentos las peliculas en el mes especificado
    cantidad = len(peliculas_mes)


    return f"{cantidad} peliculas fueron estrenadas en el mes de {mes}"


