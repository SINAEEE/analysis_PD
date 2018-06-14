
from urllib.parse import urlencode
from .json_request import json_request
import math
from datetime import datetime


ENDPOINT = "http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList"
SERVICE_KEY ="L67Cl24axIN5YZAkFU4c9ZVT3%2B%2FS8nzuC%2FDCnoEpzgFZKHkq%2B0vGkNeNbnYbhmLRtnkmzxyNOnwT9RdcFULAGA%3D%3D"


def pd_gen_url(endpoint=ENDPOINT, service_key=SERVICE_KEY, **params):
    return '%s?%s&serviceKey=%s' % (endpoint, urlencode(params), service_key)
#->service key자체는 encoding된 상태기때문에 또 encoding해주면 안됨


def pd_fetch_foreigner_visitor(country_code, year, month):
       endpoint = "http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList"
       url = pd_gen_url(endpoint,
                        YM='{0:04d}{1:02d}'.format(year, month),
                        NAT_CD=country_code,
                        ED_CD='E',
                        _type='json'
                     )

       json_result = json_request(url=url)

       json_response = json_result.get('response')
       json_header = json_response.get('header')

       result_message = json_header.get('resultMsg')

       if 'OK' != result_message:
           print('%s Error [%s] for request %s' % (datetime.now), result_message, url)
           return None

       json_body = json_response.get('body')
       json_items = json_body.get('items')

       return json_items.get('item') if isinstance(json_items,dict) else None



def pd_fetch_tourspot_visitor(district1='', district2='', tourspot='', year=0, month=0):

      isNext = True
      json_pg=1

      while isNext:
         url = pd_gen_url(
              YM='{0:04d}{1:02d}'.format(year, month),
              SIDO=district1,
              GUNGU=district2,
              RES_NM=tourspot,
              numOfRows=10,
              _type='json',
              pageNo=json_pg
          )

         json_result = json_request(url=url)

         #get메소드를 이용해서 값을 종류별로 나눠서 변수에 저장
         json_response = json_result.get('response')
         #json_header = json_response.get('header')
         #json_remsg = json_header.get('resultMsg')

         #if json_remsg is not 'OK':
         #    break

         json_body = json_response.get('body')
         json_rows = json_body.get('numOfRows')
         json_total = json_body.get('totalCount')
         json_pg = json_body.get('pageNo')

        #numOfRows를 넘어가는 내용이 있으면 다음페이지에서 출력하도록 해주는 구문
         if math.ceil(json_total/json_rows) == json_pg:
            isNext = False
         else:
            json_pg +=1

         json_items = json_body.get('items')


         yield json_items.get('item')
         #return json_items.get('item') if isinstance(json_items, dict) else None

