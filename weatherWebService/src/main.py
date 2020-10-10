import csv
from getWeather import GetWeather
from outputFormat import OutputFormat
from iata import getCityName
import time

def request_cache(city, cache, petitions):
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
    
    initial_time = time.time()
    
    initial_time_csv1 = time.time()
    info_csv('../csv/dataset1.csv')
    final_time_csv1 = time.time()
    time_csv1 = (final_time_csv1 - initial_time_csv1) / 60

    initial_time_csv2 = time.time()
    info_csv('../csv/dataset2.csv')
    final_time_csv2 = time.time()
    time_csv2 = (final_time_csv2 - final_time_csv1) / 60
    
    final_time = time.time()
    time = (final_time - initial_time) / 60

    print('\nExcecution time for csv1: ' + str(time_csv1) + 'minutes.')
    print('Excecution time for csv2: ' + str(time_csv2) + 'minutes.')
    print('\nExecution time: ' + str(time) + 'minutes')