

import collect


if __name__ == '__main__':

    # 데이터 수집(collection)

# 1) 관광지 방문객 정보
    #collect.crawlling_tourspot_visitor(district='서울특별시',start_year=2017,end_year=2017)
    collect.crawlling_tourspot_visitor('서울특별시',2017,2017)


"""
# 2) 기간,방문객 국가의 검색조건에 따른 출입국자 수 
    for country in [('중국',112),('일본',130),('미국',275)]:
            collect.crawlling_foreigner_visitor(country,2017,2017)
"""


    #데이터 분석(analysis)
    #데이터 시각화 (visualization)


