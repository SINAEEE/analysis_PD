
import os
import json
from .api import api

RESULT_DIRECTORY = '__results__/crawling'


def preprocess_foreign_visitor(data):

    #필요없는 데이터 지우기
    del data['ed']
    del data['edCd']
    del data['rnum']

    #나라코드
    data['country_code'] = data['natCd']
    del data['natCd']

    #나라 이름
    data['country_Name'] = data['natKorNm'].replace(' ','')
    del data['natKorNm']

    #방문자 수
    data['visit_counter'] = data['num']
    del data['num']

    #년월
    if 'ym' not in data:
        data['date'] = ''
    else:
        data['date'] = data['ym']
        del data['ym']


"""
def  preprocess_tourspot_visitor(item): #데이터전처리 : 공개할필요없는 함수
    #내국인 수
    if 'addrCd' not in item:
        item['count_locals'] = 0
    else:
        item['count_locals'] = item['addrCd']

    #외국인 수
    if 'csForCnt' not in item:
        item['count_foreigner']=0
    else:
        item['count_foreigner']=item['csForCnt']

    #spot
    if 'resNm' not in item:
        item['tourist_spot'] = 0
    else:
        item['tourist_spot'] = item['resNm']

    #date
    if 'ym' not in item:
        item['date'] = 0
    else:
        item['date'] = item['ym']

    #시, 도
    if 'sido' not in item:
        item['restrict1'] = 0
    else:
        item['restrict1'] = item['sido']

    #군,구
    if 'gungu' in item:
        item['restrict2'] = 0
    else:
        item['restrict2'] = item['gungu']
"""


def crawlling_foreigner_visitor(country, start_year, end_year):

    results = []

    for year in range(start_year,end_year+1):
        for month in range(1,13):
            #print("fetching.." + country[0] + ":" + str(year) + "-" + str(month))
                data = api.pd_fetch_foreigner_visitor(country[1],year,month)
                #print(data)
                if data is None:
                    continue

                preprocess_foreign_visitor(data)
                #results += data
                results.append(data)

    #save data to file
    print(results)




def crawlling_tourspot_visitor(district, start_year, end_year):

    results = []
    filename = '%s_%s_%s_%s.json' % (RESULT_DIRECTORY,district,start_year,end_year)

    for items in api.pd_fetch_tourspot_visitor(district, start_year, end_year):
        for item in items:
            preprocess_post(item)

        results += items

    # save results to file(저장/적재)
    with open(filename, 'w', encoding='utf-8') as outfile:
        json_string = json.dumps(results, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(json_string)

if os.path.exists(RESULT_DIRECTORY) is False:
    os.makedirs(RESULT_DIRECTORY)
