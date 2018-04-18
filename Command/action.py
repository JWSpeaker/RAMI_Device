from .date import GetDatetime

def case1(x):
    return {
        '오늘날씨' : 'test',
        '현재시간' : GetDatetime()
    }.get(x, 'not defined case')


def Action(command):
    return case1(command)
