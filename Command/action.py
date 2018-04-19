from .date import GetDatetime
from .weather import GetWeatherInfo
def case(x):
    return {
        '오늘날씨' : GetWeatherInfo(),
        '현재시간' : GetDatetime(),
        '종료' : 'exit'
    }.get(x, 'not defined command')


def Action(command):
    return case(command)
