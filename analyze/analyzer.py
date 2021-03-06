import json
import pandas as pd
import scipy.stats as ss
import matplotlib.pyplot as plt
import math


def analysis_correlation(resultfiles):
    with open(resultfiles['tourspot_visitor'], 'r', encoding='utf-8') as infile:
        json_data = json.loads(infile.read())

    tourspotvisitor_table = pd.DataFrame(json_data, columns=['count_foreigner', 'date', 'tourist_spot'])
    temp_tourspotvisitor_table = pd.DataFrame(tourspotvisitor_table.groupby('date')['count_foreigner'].sum())
    #print(temp_tourspotvisitor_table)

    results = []
    for filename in resultfiles['foreign_visitor']:
        with open(filename, 'r', encoding='utf-8') as infile:
            json_data = json.loads(infile.read())
            foreignvisitor_table = pd.DataFrame(json_data, columns=['country_Name','date', 'visit_counter'])
            foreignvisitor_table = foreignvisitor_table.set_index('date')
            #print(foreignvisitor_table)

            merge_table = pd.merge(
                temp_tourspotvisitor_table,
                foreignvisitor_table,
                left_index=True, right_index=True
            )

            x = list(merge_table['visit_counter'])
            y = list(merge_table['count_foreigner'])
            country_name = foreignvisitor_table['country_Name'].unique().item(0)
            #unique():중복된 값제거, item(0) : 값만 출력,['']제거
            r = ss.pearsonr(x,y)[0]
            results.append({'x': x, 'y': y, 'country_name': country_name, 'r': r})

    return results



def analysis_correlation_by_tourspot(resultfiles):
    with open(resultfiles['tourspot_visitor'], 'r', encoding='utf-8') as infile:
        json_data = json.loads(infile.read())

    tourspotvisitor_table = pd.DataFrame(json_data, columns=['count_foreigner', 'date', 'tourist_spot'])
    tourist_spot = tourspotvisitor_table['tourist_spot'].unique()
    #temp_table = tourspotvisitor_table[tourspotvisitor_table['tourist_spot'] == '경복궁']
    #temp_table = temp_table.set_index('date')
    #print(temp_table)

    results=[]
    for spot in tourist_spot:
        temp_table = tourspotvisitor_table[tourspotvisitor_table['tourist_spot'] == spot]
        temp_table = temp_table.set_index('date')
        r = []
        for filename in resultfiles['foreign_visitor']:
            with open(filename, 'r', encoding='utf-8') as infile:
                json_data = json.loads(infile.read())
            foreignvisitor_table = pd.DataFrame(json_data, columns=['country_Name', 'date', 'visit_counter'])
            foreignvisitor_table = foreignvisitor_table.set_index('date')

            merge_table = pd.merge(
                temp_table,
                foreignvisitor_table,
                left_index=True, right_index=True
            )

            y = list(merge_table['visit_counter'])  # 총 방문자수
            x = list(merge_table['count_foreigner'])  # 외국인방문객수
            # 수정필요 : x->외국인방문객수, y->총방문자수
            # -> 스팟에 대한 방문객수가 늘어날수록 총 방문자수가 늘어날것이기 떄문
            # country_name = foreignvisitor_table['country_Name'].unique().item(0)
            tourist_spot = temp_table['tourist_spot'].unique().item(0)
            r.append(correlation_coefficient(x, y))

        results.append({"tourspot": tourist_spot, "r_중국": r[0], "r_일본": r[1], "r_미국": r[2]})
        #print(results)
    return results


def correlation_coefficient(x, y):
    n = len(x)
    vals = range(n)

    x_sum = 0.0
    y_sum = 0.0
    x_sum_pow = 0.0
    y_sum_pow = 0.0
    mul_xy_sum = 0.0

    for i in vals:
        mul_xy_sum = mul_xy_sum + float(x[i]) * float(y[i])
        x_sum = x_sum + float(x[i])
        y_sum = y_sum + float(y[i])
        x_sum_pow = x_sum_pow + pow(float(x[i]), 2)
        y_sum_pow = y_sum_pow + pow(float(y[i]), 2)

    try:
        r = ((n * mul_xy_sum) - (x_sum * y_sum)) / \
            math.sqrt(((n * x_sum_pow) - pow(x_sum, 2)) * ((n * y_sum_pow) - pow(y_sum, 2)))
    except ZeroDivisionError:
        r = 0.0

    return r
