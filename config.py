import os

#configuration

CONFIG = {
    'district' : '서울특별시',
    'countries' : [('중국',112),('일본',130),('미국',275)],
    'common' : {
        'start_year' : 2017,
        'end_year' : 2017,
        'fetch' : False,
        'result_directory' : '__results__/crawlling',
        'service_key' : "L67Cl24axIN5YZAkFU4c9ZVT3%2B%2FS8nzuC%2FDCnoEpzgFZKHkq%2B0vGkNeNbnYbhmLRtnkmzxyNOnwT9RdcFULAGA%3D%3D"
    }
}

if not os.path.exists(CONFIG['common']['result_directory']):
    os.makedirs(CONFIG['common']['result_directory'])

