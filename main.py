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



dias_semana = {
    "lunes": "Monday", "martes": "Tuesday", "miércoles": "Wednesday", "miercoles": "Wednesday", "jueves": "Thursday", "viernes": "Friday", 
    "sábado": "Saturday", "sabado": "Saturday", "domingo": "Sunday"
}

@app.get('/cantidad_filmaciones_dia/{dia}')
async def cantidad_filmaciones_dia(dia: str):

    #Convierto a minuscula y quito acentos
    dia = dia.lower().replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u') 

    #Verifico si el dia ingresado es correcto
    if dia not in dias_semana:
        return f"Error: {dia} no es válido. Por favor, ingrese un dia de la semana en español"
    
    #Obtengo el nombre de los dias en Inglés
    day_name = dias_semana[dia]
    
    #Filtro las peliculas por dia
    peliculas_dia = df_movies[df_movies['release_date'].dt.day_name() == day_name]

    #Cuento las peliculas
    cantidad = len(peliculas_dia)

    return f"{cantidad} peliculas fueron estrenadas el {dia}"