

import collect


if __name__ == '__main__':

    # 데이터 수집(collection)
    """
    collect.crawlling_tour_spot_visitor(district='서울특별시',
                                       start_year=2017,
                                       end_year=2017)
    """

    for country in [('중국',112),('일본',130),('미국',275)]:
            collect.crawlling_foreigner_visitor(country,2017,2017)


    #데이터 분석(analysis)
    #데이터 시각화 (visualization)


