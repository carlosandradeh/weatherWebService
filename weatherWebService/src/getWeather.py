from request import Request

class GetWeather:

    @staticmethod
    def get_info(city):
        """
        Static Method for the city format of the program's output.
        :param city: City name for the request to the weather API
        :return: String
        """
        #Hacemos la petición a la Api
        result = Request.requests(city)
        if result != 'Error':
            #Obtenemos los valores que necesitamos.
            city = ' City: ' + city
            description = ' Description: ' + result['description'] 
            temp = ' Temperature: ' + str(result['temp']) + "°C"
            temp_max = ' MaxTemperature: ' + str(result['temp_max']) + "°C"
            temp_min = ' MinTemperature: ' + str(result['temp_min']) + "°C"
            humidity = ' Humidity: ' + str(result['humidity'])
            info = city + description + temp + temp_max + temp_min + humidity + '\n'
            return info
        else : 
            return ' City not found ' + city


