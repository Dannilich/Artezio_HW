"""
Модуль по аолучения ответа сервера
"""
import requests

def get_response(url: "url of web-site") -> "request: GET request":
    """make GET request and return response"""
    return requests.get(url)

#print(get_response.__annotations__)
