
from analysis_PD.collect.api import api as pdapi


"""
# test for ps_gen_url
url = pdapi.pd_gen_url(
    "http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList",
    "L67Cl24axIN5YZAkFU4c9ZVT3%2B%2FS8nzuC%2FDCnoEpzgFZKHkq%2B0vGkNeNbnYbhmLRtnkmzxyNOnwT9RdcFULAGA%3D%3D",
    YM='{0:04d}{1:02d}'.format(2017, 1),
    SIDO='서울특별시', 
    GUNGU='', 
    RES_NM='', 
    numOfRows=100, 
    _type='json', 
    pageNo=20
)
print(url) 
"""


for item in pdapi.pd_fetch_tourspot_visitor(district1='서울특별시', year=2017, month=1):
    print(item)

"""
# test from pd_fetch_tourspot_visitor
for year in range(2017, 2018):
    for month in range(1, 13):
        for item in pdapi.pd_fetch_tourspot_visitor(
                district1='서울특별시',
                year=year,
                month=month):
            print(item)
"""

