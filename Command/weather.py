import requests
from xml.etree.ElementTree import parse

key = "uM2qc4IfnnDweWL6KMfASJaR2%2FNqQbyUBp18IE607JJsn%2B4qm6Bu8hwpPSdI88N97b%2Btm988xzBrDpEZAuVpgA%3D%3D"
url = "http://newsky2.kma.go.kr/service/VilageFrcstDspthDocInfoService/WidGeneralWeatherCondition?"

def GetWeatherInfo():
    headers = {
        "serviceKey" : key,
        "regId" : "11D10401"
    }
    print('key ' + key)
    res = requests.get(url= "http://newsky2.kma.go.kr/service/VilageFrcstDspthDocInfoService/WidOverlandForecast?serviceKey=uM2qc4IfnnDweWL6KMfASJaR2%2FNqQbyUBp18IE607JJsn%2B4qm6Bu8hwpPSdI88N97b%2Btm988xzBrDpEZAuVpgA%3D%3D&regId=11A00101&numOfRows=10&pageSize=10&pageNo=1&startPage=1")
    result = res.text

    tree = parse(result)
    note=tree.getroot()

    print(result)


if __name__ == "__main__":
    GetWeatherInfo();
