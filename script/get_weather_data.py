import sys
import os
sys.path.append("..")
print(sys.path)
parentdir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
 #把目录加入环境变量
sys.path.insert(0, parentdir)
import requests
from utils.const_value import API, KEY, UNIT, LANGUAGE
from utils.helper import getLocation


def fetchWeather(location):
    result = requests.get(API, params={
        'key': KEY,
        'location': location,
        'language': LANGUAGE,
        'unit': UNIT
    }, timeout=1)
    return result.text


if __name__ == '__main__':
    location = getLocation()
    result = fetchWeather(location)
    print(result)
