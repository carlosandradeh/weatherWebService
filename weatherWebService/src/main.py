import csv
from getWeather import GetWeather
from outputFormat import OutputFormat
from iata import getCityName
import time

def request_cache(city, cache, petitions):
    """
    Method to make a request if the city is not in the cache and return their weather info in a string; if the 
    city is in the request then just return the info weather string on the key of the cache.
    :param city: The name of the city 
    :param cache: The dictionary (HashTable) where the info is collect.
    :param petitions: The number o petitions to the OpenWeather API.
    :return info_city: A String with the current weather info o a city. 
    """
    #Si la ciudad no está en el diccionario Cache entonces hará una consulta y agregará la info al Cache.
    if city not in cache:
        info_city = GetWeather.get_info(city)
        cache.setdefault(city, info_city)
        petitions = petitions + 1
    else: #De otro modo obtendrá la información del diccionario cache.
        info_city = cache.get(city)

    #Retornará la información del clima de la ciudad.
    return info_city


def info_csv(path):
    """
        Method to open a csv file and print the weather info of each origin city and destination city in the csv.
        :param path: The url of the csv file.

    """
    petitions = 0
    cache = {}
    
    try:
        #Abrimos el CSV en la ruta dada
        with open(path) as f:
            reader = csv.DictReader(f) #Obtenemos el Iterable con cada fila como diccionario.
        
            for row in reader:

                #Del diccionario de cada fila obtenemos el origen (default mex) y el origen.
                origin = row.get('origin', 'MEX')
                destination = row.get('destination', row.get('destino'))

                if 'origin' in row:
                    origin = getCityName(origin)
                    destination = getCityName(destination)

                #Obtenemos la información del clima del origen y del destino.        
                info_origin = request_cache(origin, cache, petitions)
                info_destination = request_cache(destination, cache, petitions)

                if petitions == 58:
                    time.sleep(60)
                    petitions = 0
                
                #Le daremos formato a la información y la imprimiremos.
                out = OutputFormat.output_format(info_origin,info_destination)
                print(out)

    except FileNotFoundError as error:
        print('File not found: ' + path)

    
            


if __name__ == '__main__':
    info_csv('../csv/dataset1.csv')
    info_csv('../csv/dataset2.csv')