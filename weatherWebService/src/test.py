"""
    assert <contiditon>, <optional-message> 
"""
from request import Request
from getWeather import GetWeather


def test_correct_city_name_request():
    error_message = 'Error'
    fail_message = 'Prove Correct City Name Request Fail'

    correct_city_name = 'Mexico'
    request_correct_city_name = Request.requests(correct_city_name)
    assert request_correct_city_name != error_message, fail_message
    return True

def test_incorrect_city_name_request():
    error_message = 'Error'
    fail_message = 'Prove Incorrect City Name Request Fail'
    
    incorrect_city_name = 'Incorrect City Name'
    request_incorrect_city_name = Request.requests(incorrect_city_name)
    assert request_incorrect_city_name == error_message, fail_message
    return True

def test_correct_iata_code_request():
    error_message = 'Error'
    fail_message = 'Prove Correct Iata Code Request Fail'
    
    correct_iata_code = 'BOG'
    request_correct_iata_code = Request.requests(correct_iata_code)
    assert request_correct_iata_code != error_message, fail_message
    return True

def test_incorrect_iata_code_request():
    error_message = 'Error'
    fail_message = 'Prove Incorrect Iata Code Request Fail'
    
    incorrect_iata_code = 'IAC'
    request_incorrect_iata_code = Request.requests(incorrect_iata_code)
    assert request_incorrect_iata_code == error_message, fail_message
    return True

if __name__ == '__main__':
    test_correct_city = 'Passed' if test_correct_city_name_request() else 'Fail'
    test_incorrect_city = 'Passed' if test_incorrect_city_name_request() else 'Fail'
    test_correct_iata = 'Passed' if test_correct_iata_code_request() else 'Fail'
    test_incorrect_iata = 'Passed' if test_incorrect_iata_code_request() else 'Fail'

    print('Test Request Correct City Name: ', test_correct_city )
    print('Test Request Incorrect City Name: ', test_incorrect_city)
    print('Test Request Correct Iata Code: ', test_correct_iata )
    print('Test Request Incorrect Iata Code: ', test_incorrect_iata)