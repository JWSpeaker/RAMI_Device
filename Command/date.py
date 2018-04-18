
import datetime

def GetDatetime():
    now = datetime.datetime.now()
    return '%s월 %s일 %s시 %s분입니다.' % (now.month, now.day, now.hour, now.minute)


if __name__ == "__main__":
    print(GetDatetime())
