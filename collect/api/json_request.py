import sys
from urllib.request import Request, urlopen
from datetime import *
import json


def json_request(
        url='',
        encoding='utf-8', #문자열을 바이트로 전환
        success=None,
        error=lambda e: print('%s : %s' % (e, datetime.now()), file=sys.stderr)):
    try:
        # 매개변수로 받은 url에 json 요청을 보내고 그 응답으로 json을 리턴받아 처리
        request = Request(url)

        #urllib.request.Request 사용시 json문자열이아닌 json바이트배열로 주고 받아야함
        resp = urlopen(request)

        resp_body = resp.read().decode(encoding) #decode:바이트를 문자열로 변환


        json_result = json.loads(resp_body)

        print('%s : success for request [%s]' % (datetime.now(), url))

        if callable(success) is False:
            return json_result

        success(json_result)



    except Exception as e:
        callable(error) and error(e)
