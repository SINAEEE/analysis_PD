#import os
import json
from .api import api

#RESULT_DIRECTORY = '__results__/crawlling'


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



def preprocess_tourspot_visitor(item): #데이터전처리 : 공개할필요없는 함수

    #필요없는 항목 지우기
    del item['addrCd']
    del item['rnum']

    #내국인 수
    item['count_locals'] = item['csNatCnt']
    del item['csNatCnt']

    #외국인 수
    item['count_foreigner'] = item['csForCnt']
    del item['csForCnt']

    #spot
    item['tourist_spot'] = item['resNm']
    del item['resNm']

    #date
    item['date'] = item['ym']
    del item['ym']

    #시, 도
    item['restrict1'] = item['sido']
    del item['sido']

    #군,구
    item['restrict2'] = item['gungu']
    del item['gungu']


def crawlling_foreigner_visitor(country,
                                start_year,
                                end_year,
                                fetch=True,
                                result_directory='',
                                service_key=''):

    results = []

    if fetch:
        for year in range(start_year,end_year+1):
            for month in range(1,13):
                #print("fetching.." + country[0] + ":" + str(year) + "-" + str(month))
                    data = api.pd_fetch_foreigner_visitor(country[1],
                                                          year,
                                                          month,
                                                          service_key)
                    #print(data)
                    if data is None:
                        continue

                    preprocess_foreign_visitor(data)
                    #results += data
                    results.append(data)

    # save results to file(저장/적재)
    filename = '%s/%s(%s)_foreign_visitor_%s_%s.json' % (result_directory,country[0],country[1],start_year,end_year)
    with open(filename, 'w', encoding='utf-8')as outfile:
        json_string = json.dumps(results, indent=4, sort_keys=True, ensure_ascii=False) #indent:들여쓰기
        outfile.write(json_string)


#if not os.path.exists(RESULT_DIRECTORY):
#   os.makedirs(RESULT_DIRECTORY)




def crawlling_tourspot_visitor(district,
                               start_year,
                               end_year,
                               fetch=True,
                               result_directory='',
                               service_key=''):

    results = []
    filename = '%s/%s_touristspot_%s_%s.json' % (result_directory, district, start_year, end_year)

    if fetch:
        for year in range(start_year, end_year+1):
            for month in range(1, 13):
                 for item in api.pd_fetch_tourspot_visitor(district1=district,
                                                           year=year,
                                                           month=month,
                                                           service_key=service_key):
                    for i in item:
                        #print(item)
                        #if i is None:
                         #   continue
                        #print(type(item),item)
                        preprocess_tourspot_visitor(i)

                    results.append(i)


    # save results to file(저장/적재)

        with open(filename, 'w', encoding='utf-8') as outfile:
            json_string = json.dumps(results, indent=4, sort_keys=True, ensure_ascii=False)
            outfile.write(json_string)

    return filename

#if os.path.exists(RESULT_DIRECTORY) is False:
#    os.makedirs(RESULT_DIRECTORY)
