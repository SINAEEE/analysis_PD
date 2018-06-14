
from analysis_PD.collect.api import api as api


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



#test for pd_fetch_tourspot_visitor

for item in api.pd_fetch_tourspot_visitor(district1='서울특별시', year=2017, month=1):
    print(item)



"""
#test for pd_fetch_foreigner_visitor
#from .api import pd_fetch_foreigner_visitor #api디렉토리 init파일에넣어주기?

item = api.pd_fetch_foreigner_visitor(112, 2012,7)
print(item)
"""
