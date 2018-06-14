
# Test for web_request.json_request

from collect.api import json_request as jr

url ='http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList?serviceKey=L67Cl24axIN5YZAkFU4c9ZVT3%2B%2FS8nzuC%2FDCnoEpzgFZKHkq%2B0vGkNeNbnYbhmLRtnkmzxyNOnwT9RdcFULAGA%3D%3D&_type=json'

"""
# 3방식
def error_fetch_user_list(e):
    print(e)

wr.json_request(url=url, error=error_fetch_user_list)
"""



# 2 방식
def sucess_fetch_userlist(response):
    print(response)

jr.json_request(url=url, success=sucess_fetch_userlist)


"""
#1 방식
json_result = jr.json_request(url)
print(json_result)
"""

