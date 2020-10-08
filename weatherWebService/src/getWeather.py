from request import Request

class getWeather:

    @staticmethod
    def getInfo(city):
        """
        Method for the city format of the program's output.
        :param city: Iata code for the request to the weather API
        :return: String
        """
        result = Request.requests(city)
        if result != 'Errooor':
            city = ' City: ' + city
            temp = ' Temperature: ' + str(result['temp'])
            temp_max = ' Max Temperature: ' + str(result['temp_max'])
            temp_min = ' Min Temperature: ' + str(result['temp_min'])
            info = city + temp + temp_max + temp_min
            return info
        else : 
            return 'City not found'
        
        

    @staticmethod
    def outputFormat(destination, origin='mex'):
        """
        Method for the format of the program's output.
        :param destination: Iata code of the destination city for the request to the weather API
        :param origin: Iata code of the origin city for the request to the weather API
        :return: String
        """
        origin_format = getWeather.getInfo(origin)
        destination_format = getWeather.getInfo(destination)
        f = 'ORIGIN:\n' + origin_format + '\nDESTINATION:\n' + destination_format
        return f

