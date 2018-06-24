import collect
import analyze
import visualize
from config import CONFIG



if __name__ == '__main__':

    # 데이터 수집(collection)

    # 1) 관광지 방문객 정보
    #collect.crawlling_tourspot_visitor( district=CONFIG['district'], **CONFIG['common'])

    resultfiles = dict()

    resultfiles['tourspot_visitor'] = collect.crawlling_tourspot_visitor(district=CONFIG['district'],
                                                                         **CONFIG['common'])

    # 2) 기간,방문객 국가의 검색조건에 따른 출입국자 수
    """
    for country in CONFIG['countries']:
        collect.crawlling_foreigner_visitor(country, **CONFIG['common'])
    """

    resultfiles['foreign_visitor'] = []
    for country in CONFIG['countries']:
        rf = collect.crawlling_foreigner_visitor(country, **CONFIG['common'])
        resultfiles['foreign_visitor'].append(rf)

    #print(resultfiles)


    #1. analysis and visualize

    #result_analysis = analyze.analysis_correlation(resultfiles)
    #print(len(resultfiles))
    #print(result_analysis)
    #visualize.graph_scatter(result_analysis)


    #2. analysis and visualize

    result_analysis = analyze.analysis_correlation_by_tourspot(resultfiles)
    #print(type(result_analysis))
    visualize.graph_bar(result_analysis)


    #graph_table = pd.DataFrame(result_analysis, colums=['tourspot','r_중국','r_일본','r_미국'])
    #graph_table = graph_table.set_index('tourspot')
    
    #graph_table.plot(kind='bar')
    #plt.show()




