
from urllib.parse import urlencode
from .json_request import json_request
from datetime import datetime
import sys
import math


ENDPOINT = "http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList"
SERVICE_KEY ="L67Cl24axIN5YZAkFU4c9ZVT3%2B%2FS8nzuC%2FDCnoEpzgFZKHkq%2B0vGkNeNbnYbhmLRtnkmzxyNOnwT9RdcFULAGA%3D%3D"


def pd_gen_url(endpoint=ENDPOINT, service_key=SERVICE_KEY, **params):
    return '%s?%s&serviceKey=%s' % (endpoint, urlencode(params), service_key)

def pd_fetch_tourspot_visitor(district1='', district2='', tourspot='', year=0, month=0):

      isNext = True
      json_pg=1
      while isNext is True:

         url = pd_gen_url(
              # ENDPOINT,
              YM='{0:04d}{1:02d}'.format(year, month),
              SIDO=district1,
              GUNGU=district2,
              RES_NM=tourspot,
              numOfRows=10,
              _type='json',
              pageNo=json_pg
              # service_key=SERVICE_KEY
          )

         json_result = json_request(url=url)

         json_response = json_result.get('response')
         #json_header = json_response.get('header')
         #json_remsg = json_header.get('resultMsg')

         #if json_remsg is not 'OK':
         #    break

         json_body = json_response.get('body')
         json_rows = json_body.get('numOfRows')
         json_total = json_body.get('totalCount')
         json_pg = json_body.get('pageNo')

         if math.ceil(json_total/json_rows) == json_pg:
            isNext = False
         else:
            json_pg +=1

         json_items = json_body.get('items')

         yield json_items.get('item')

































