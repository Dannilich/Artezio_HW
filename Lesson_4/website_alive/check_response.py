"""
Модуль по проверки ответа сервера
"""
import website_alive.make_request as make_request

def check_response(url: "url of web-site")->"bool: response is 200 OK ?":
    """make GET request and check response is 200 OK"""
    return make_request.get_response(url).ok

#print(check_response.__annotations__)
