import requests

class Request:

    appid = 'd3b410cd42f3274d6bcd98f7f671d422'

    @classmethod
    def requests(cls, city):

        """
            Class Method to make a request with the name of a city, witch return a hash table with 
            the info of the weather of the city in it if the status_code is succesfull.
            :param city: name of a city.
            :return: Hash table with a weather information of a city.
        """

        url = 'https://api.openweathermap.org/data/2.5/weather'
        args = {'q': city, 'units':'metric', 'appid': cls.appid}

        response = requests.get(url, params=args)

        if response.status_code == 200:
            payload = response.json() #Nos regresará un Diccionario que será el JSON.
            main = payload.get('main', []) #Obtendremos el diccionario con las entradas de "main".
            weather = payload.get('weather', [])[0] #Obtendremos el diccionario con las entradas de "weather".
            main.update(weather) #Juntamos los dos diccionarios para trabajar con él.
            return main
        else:
            return "Error"
