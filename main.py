import collect
from config import CONFIG


if __name__ == '__main__':

    # 데이터 수집(collection)

# 1) 관광지 방문객 정보
    collect.crawlling_tourspot_visitor(CONFIG['district'],
                                       # 아래 두줄 대신 한줄로 쓸수있음 (서비스키까지 들어온것)
                                       # start_year=CONFIG['common']['start_year'],
                                       # end_year=CONFIG['common']['end_year']
                                       **CONFIG['common']
                                       )
    #collect.crawlling_tourspot_visitor(country, **CONFIG['common'])



# 2) 기간,방문객 국가의 검색조건에 따른 출입국자 수 
    for country in CONFIG['countries']:
            collect.crawlling_foreigner_visitor(country,**CONFIG['common'])



    #데이터 분석(analysis)
    #데이터 시각화 (visualization)


