import requests
import json
import datetime


key = "uM2qc4IfnnDweWL6KMfASJaR2%2FNqQbyUBp18IE607JJsn%2B4qm6Bu8hwpPSdI88N97b%2Btm988xzBrDpEZAuVpgA%3D%3D"


def GetWeatherInfo():
    url = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastGrib"

    now = datetime.datetime.now()

    if now.strftime("%M") < "45" :
        now = now - datetime.timedelta(hours=1)
    params = {
        "base_date" : now.strftime("%Y%m%d"),
        "base_time" : now.strftime("%H") +"30",
        "nx" : "60",
        "ny" : "127",
        "numOfRows" : "10",
        "pageNo" : "1",
        "_type" : "json"
    }
    url = url + "?ServiceKey=" + key
    res = requests.get(url= url, params = params)
    result = res.text

    jsonData = json.loads(result)

    curr_temp = ""
    curr_sky = ""

    for element in jsonData["response"]["body"]["items"]["item"] :
        #print(element)
        if element["category"] =='SKY':
            curr_sky = element["obsrValue"]
        elif element["category"] == 'T1H':
            curr_temp = element["obsrValue"]

    #print("curr temp : " + str(curr_temp))
    #print("curr sky : " + str(curr_sky))

    sky_str = ""
    if curr_sky == 1:
        sky_str = "맑으며 "
    elif curr_sky == 2:
        sky_str = "구름이 조금 끼겠으며 "
    elif curr_sky ==3:
        sky_str = "구름이 대체로 많겠으며 "
    else:
        sky_str = "흐리며 "

    #"현재 맑으며 기온은 ㅇㅇ도입니다. 오늘은 대체로 맑을 전망입니다 최고기온은 ㅇㅇㄷ 최저기온은 ㅇㅇ입니다. 현재 미세먼지 농도는 보통단계입니다."
    return "현재 " + str(sky_str) + "기온은 " + str(curr_temp) + "도 입니다."


if __name__ == "__main__":
    print(GetWeatherInfo());
