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
    #print(tourspotvisitor_table)
    #print(temp_tourspotvisitor_table)

    results = []
    for filename in resultfiles['foreign_visitor']:
        with open(filename, 'r', encoding='utf-8') as infile:
            json_data = json.loads(infile.read())
        foreignvisitor_table = pd.DataFrame(json_data, columns=['country_name','date', 'visit_counter'])
        foreignvisitor_table = foreignvisitor_table.set_index('date')

        merge_table = pd.merge(
            temp_tourspotvisitor_table,
            foreignvisitor_table,
            left_index=True, right_index=True)

        x = list(merge_table['visit_counter']) #방문자수
        y = list(merge_table['count_foreigner']) #외국인수
        country_name = foreignvisitor_table['country_name'].unique().item(0)
        #print(x)
        #print(y)
        r = ss.pearsonr(x, y)[0] #튜플값이 나옴
        # r = np.corrcoef(x, y)[0]
        results.append({'x': x, 'y': y, 'country_name': country_name, 'r': r})


        #merge_table['visit_counter'].plot(kind='bar')
        #plt.show()

    return results



def analysis_correlation_by_tourspot(resultfiles):
    with open (resultfiles['tourspot_visitor'], 'r', encoding='utf-8') as infile:
        json_data = json.loads(infile.read())

        tourspotvisitor_table = pd.DataFrame(json_data, columns=['count_foreigner', 'date', 'tourist_spot'])
        tourist_spot = tourspotvisitor_table['tourist_spot'].unique()
        #temp_table = tourspotvisitor_table[tourspotvisitor_table['tourist_spot']=='경복궁']
        #print(temp_table)

        results = []
        for spot in tourist_spot:
            temp_table = tourspotvisitor_table[tourspotvisitor_table['tourist_spot'] == spot]
            #temp.append(temp_table)
            #print(temp)
            for filename in resultfiles['foreign_visitor']:
                with open(filename, 'r', encoding='utf-8')as infile:
                    json_data = json.loads(infile.read())
                foreignvisitor_table = pd.DataFrame(json_data,columns=['country_Name','visit_counter'])
                #temp.append(foreignvisitor_table)

                merge_table = pd.merge(
                    temp_table,
                    foreignvisitor_table,
                    left_index=True, right_index=True)

                results.append(merge_table)
                print(merge_table)



        #return temp



        results = []
        for filename in resultfiles['foreign_visitor']:
            with open(filename, 'r', encoding='utf-8') as infile:
                json_data = json.loads(infile.read())
            foreignvisitor_table = pd.DataFrame(json_data, columns=['country_Name', 'date', 'visit_counter'])
            foreignvisitor_table = foreignvisitor_table.set_index('date')

            """
            merge_table = pd.merge(
                temp_tourspotvisitor_table,
                foreignvisitor_table,
                left_index=True, right_index=True)
            """

        #print(foreignvisitor_table)






"""
        tourspot_table = pd.DataFrame(json_data, columns=['count_foreigner','date','tourist_spot'])
        #print(tourspot_table)
        # 관광지별 외국인수
        temp_tourspot_table = pd.DataFrame(tourspot_table.groupby('tourist_spot')['count_foreigner'].sum())
        print(temp_tourspot_table)

        results = []
        for filename in resultfiles['foreign_visitor']:
            with open(filename, 'r', encoding='utf-8') as infile:
                json_data = json.loads(infile.read())

            foreignvisitor_table = pd.DataFrame(json_data, columns=['country_Name','date','visit_counter'])

            #print(foreignvisitor_table)
            #foreignvisitor_table = foreignvisitor_table.set_index('tourist_spot')
"""






