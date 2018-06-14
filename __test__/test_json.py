
import sys
from urllib.request import Request, urlopen
from datetime import *
import json

try:
    url = 'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList?serviceKey=L67Cl24axIN5YZAkFU4c9ZVT3%2B%2FS8nzuC%2FDCnoEpzgFZKHkq%2B0vGkNeNbnYbhmLRtnkmzxyNOnwT9RdcFULAGA%3D%3D&_type=json'

    request = Request(url) # 요청
    resp = urlopen(request) # open
    resp_body = resp.read().decode("utf-8") #read

    json_result = json.loads(resp_body) #읽어들인 내용을 json으로 로드
    print(type(json_result), " : ", json_result) # type : dict, json으로 body를 읽어들인것

except Exception as e:
    print('%s %s' % (e, datetime.now), file = sys.stderr)
