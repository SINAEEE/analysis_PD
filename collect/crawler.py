
from .api import api

RESULT_DIRECTORY = '__results__/crawling'


def preprocess_post(item): #데이터전처리 : 공개할필요없는 함수
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



def crawlling_tourspot_visitor(district, start_year, end_year):

    results = []
    filename = '%s_%s_%s_%s.json' % (RESULT_DIRECTORY,district,start_year,end_year)

    for items in api.pd_fetch_tourspot_visitor(district, start_year, end_year):
        for item in items:

"""
def crawling(pagename, since, until):
    results = []
    filename = '%s_%s_%s_%s.json' % (RESULT_DIRECTORY,pagename,since,until)

    for posts in api.fb_fetch_posts(pagename, since, until):
        for post in posts: #개별전처리(50개씩받아서 하나씩)
            preprocess_post(post)

        results += posts

    #save results to file(저장/적재)
    #outfile = open(filename, 'w', encoding='utf-8')
    with open(filename, 'w', encoding='utf-8') as outfile:
        json_string = json.dumps(results, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(json_string)


if os.path.exists(RESULT_DIRECTORY) is False:
    os.makedirs(RESULT_DIRECTORY)
"""