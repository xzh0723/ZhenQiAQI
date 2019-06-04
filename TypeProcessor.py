def typeProcess(type):
    """
    处理不同类型的参数
    :return:
    """
    if type == '0':
        method = 'GETDATA'
        object_ = {
            'city': input('请输入您要查询的城市>> ')
        }
        API = 'https://www.aqistudy.cn/apinew/aqistudyapi.php'
        return method, object_, API
    if type == '1':
        method = 'GETDETAIL'
        object_ = {
            'city': input('请输入您要查询的城市>> '),
            'startTime': input('请输入您查询的起始时间（日期精确到秒，如2019-06-03 00:00:00）>> '),
            'endTime': input('请输入您查询的截至时间（日期精确到秒，如2019-06-03 23:00:00）>> '),
            'type': 'HOUR'
        }
        API = 'https://www.aqistudy.cn/apinew/aqistudyapi.php'
        return method, object_, API
    if type == '2':
        method = 'GETMAPDATA'
        object_ = {
            'timepoint': input('请输入您的查询时间（日期精确到秒，如2019-06-03 23:00:00）>> '),
            'type': 'HOUR'
        }
        API = 'https://www.aqistudy.cn/apinew/aqistudyapi.php'
        return method, object_, API
    if type == '3':
        method = 'GETPROVINCEDATA'
        object_ = {
            'timepoint': input('请输入您的查询时间（日期精确到秒，如2019-06-03 23:00:00）>> '),
            'type': 'HOUR'
        }
        API = 'https://www.aqistudy.cn/apinew/aqistudyapi.php'
        return method, object_, API
    if type == '4':
        method = 'GETCITYRANK'
        object_ = {
            'item': 'HOUR',
            'orderype': 'DESC',
            'ranktype': '169',
            'type': 'AQI'
        }
        API = 'https://m.zq12369.com/api/newzhenqiapi.php'
        return method, object_, API

    # if self.type == '全球分布':
    #    print('抱歉目前暂时未开通该服务')
    #    return None

    if type == '5':
        method = 'GET3CITYPERIOD'
        object_ = {
            'city1': input('请输入您要比较的城市1>> '),
            'city2': input('请输入您要比较的城市2>> '),
            'city3': input('请输入您要比较的城市3>> '),
            'startTime': input('请输入您查询的起始时间（日期精确到秒，如2019-06-03 00:00:00）>> '),
            'endTime': input('请输入您查询的截至时间（日期精确到秒，如2019-06-03 23:00:00）>> '),
            'type': 'HOUR'
        }
        API = 'https://www.zq12369.com/api/newzhenqiapi.php'
        return method, object_, API
    if type == '6':
        method = 'GETCITYTIME'
        object_ = {
            'city': input('请输入您要查询的城市>> '),
            'startTime': input('请输入您查询的起始时间（日期精确到秒，如2019-06-03 00:00:00）>> '),
            'endTime': input('请输入您查询的截至时间（日期精确到秒，如2019-06-03 23:00:00）>> ')
        }
        API = 'https://www.aqistudy.cn/apinew/aqistudyapi.php'
        return method, object_, API
    if type == '7':
        method = 'GETCITYMONTH'
        object_ = {
            'month': input('请输入您要查询的月份（如"2019-04") >> ')
        }
        API = 'https://www.aqistudy.cn/apinew/aqistudyapi.php'
        return method, object_, API
    if type == '8':
        method = 'GETAQIWEATHER'
        object_ = {
            'city': input('请输入您要查询的城市>> '),
            'startTime': input('请输入您查询的起始时间（日期精确到秒，如2019-06-03 00:00:00）>> '),
            'endTime': input('请输入您查询的截至时间（日期精确到秒，如2019-06-03 23:00:00）>> ')
        }
        API = 'https://www.aqistudy.cn/apinew/aqistudyapi.php'
        return method, object_, API
    if type == '9':
        method = 'GETAQIGDP'
        object_ = {
            'month': input('请输入您要查询的月份（如"2019-04") >> ')
        }
        API = 'https://www.aqistudy.cn/apinew/aqistudyapi.php'
        return method, object_, API
    else:
        print('类型输入错误，请检查后重新输入正确类型')
        print('=====' * 100)
        return '', '', ''
