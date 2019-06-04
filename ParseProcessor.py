def parseProcess(type, item):
    """
    处理清洗不同类型的数据
    :return:
    """
    if type == '0':
        data = item['result']['data']
        cityInfo = data['cityinfo']
        print(f'城市信息：{cityInfo}')
        aqi = data['aqi']
        print(f'aqi: {aqi}')
        rows = data['rows']
        if rows:
            for row in rows:
                region = row['region']
                info = {
                    'aqi': row['aqi'],
                    'pm2.5': row['pm2_5'],
                    'pm10': row['pm10'],
                    'so2': row['so2'],
                    'no2': row['no2'],
                    'co': row['co'],
                    'o3': row['o3'],
                    'complexindex': row['complexindex'],
                    'level': row['level'],
                    'quality': row['quality'],
                    'primary_pollutant': row['primary_pollutant'],
                    'ratio': row['ratio'],
                    'indexratio': row['indexratio']
                }
                print(f'{region}>> {info}')
        return

    if type == '1':
        data = item['result']['data']
        rows = data['rows']
        if rows:
            for row in rows:
                time = row['time']
                info = {
                    'rank': row['rank'],
                    'aqi': row['aqi'],
                    'pm2.5': row['pm2_5'],
                    'pm10': row['pm10'],
                    'so2': row['so2'],
                    'no2': row['no2'],
                    'co': row['co'],
                    'o3': row['o3'],
                }
                print(f'{time}>> {info}')
        return

    if type == '2':
        data = item['result']['data']
        rows = data['rows']
        if rows:
            for row in rows:
                cityName = row['cityname']
                info = {
                    'aqi': row['aqi'],
                    'pm2.5': row['pm2_5'],
                    'pm10': row['pm10'],
                    'so2': row['so2'],
                    'no2': row['no2'],
                    'co': row['co'],
                    'o3': row['o3'],
                    'primary_pollutant': row['primary_pollutant']
                }
                print(f'{cityName}>> {info}')
        return

    if type == '3':
        data = item['result']['data']
        rows = data['rows']
        print('省级行政区空气状况排名：')
        if rows[:30]:
            for row in rows[:30]:
                place = row['place']
                info = {
                    'rank': row['rank'],
                    'aqi': row['aqi'],
                    'pm2.5': row['pm2_5'],
                    'pm10': row['pm10'],
                    'so2': row['so2'],
                    'no2': row['no2'],
                    'co': row['co'],
                    'o3': row['o3'],
                    'pollutant': row['pollutant'],
                    'flag': row['flag']
                }
                print(f'    {place}省>> {info}')
        print('=====' * 100)
        print('市级行政区空气状况排名: ')
        if rows[31:]:
            for row in rows[31:]:
                place = row['place']
                info = {
                    'rank': row['rank'],
                    'aqi': row['aqi'],
                    'pm2.5': row['pm2_5'],
                    'pm10': row['pm10'],
                    'so2': row['so2'],
                    'no2': row['no2'],
                    'co': row['co'],
                    'o3': row['o3'],
                    'pollutant': row['pollutant'],
                    'flag': row['flag']
                }
                print(f'    {place}>> {info}')
        return

    if type == '4':
        data = item['result']['data']
        if data:
            for item in data:
                time = item['time']
                info = {
                    'rank': item['rank'],
                    'cityName': item['cityname'],
                    'provincename': item['provincename'],
                    'aqi': item['aqi'],
                    'primary_pollutant': item['primary_pollutant'],
                    'pm2.5': item['pm2_5'],
                    'pm10': item['pm10'],
                    'so2': item['so2'],
                    'co': item['co'],
                    'o3': item['o3'],
                    'o3_8h': item['o3_8h'],
                    'no2': item['no2'],
                    'complexindex': item['complexindex'],
                    'quality': item['quality']
                }
                print(f'{time}>> {info}')
        return

    if type == '5':
        data = item['result']['data']
        rows = data['rows']
        if rows:
            for row in rows:
                time = row['time']
                info = {
                    'rank': row['rank'],
                    'cityName': row['cityname'],
                    'aqi': row['aqi'],
                    'pm2.5': row['pm2_5'],
                    'pm10': row['pm10'],
                    'so2': row['so2'],
                    'no2': row['no2'],
                    'co': row['co'],
                    'o3': row['o3'],
                    'primary_pollutant': row['primary_pollutant'],
                    'complexindex': row['complexindex'],
                    'temp': row['temp'],
                    'humi': row['humi'],
                    'windlevel': row['windlevel'],
                    'winddirection': row['winddirection'],
                    'weather': row['weather']
                }
                print(f'{time}>> {info}')
        return

    if type == '6':
        data = item['result']['data']
        rows = data['aqi']
        if rows:
            for row in rows:
                time = row['time']
                info = {
                    'aqi': row['aqi'],
                    'pm2.5': row['pm2_5'],
                    'pm10': row['pm10'],
                    'so2': row['so2'],
                    'no2': row['no2'],
                    'co': row['co'],
                    'o3': row['o3'],
                }
                print(f'{time}>> {info}')
        return

    if type == '7':
        data = item['result']['data']
        rows = data['rows']
        if rows:
            for row in rows:
                cityName = row['cityname']
                province = row['province']
                info = {
                    'rank': row['rank'],
                    'aqi': row['aqi'],
                    'pm2.5': row['pm2_5'],
                    'pm10': row['pm10'],
                    'so2': row['so2'],
                    'no2': row['no2'],
                    'co': row['co'],
                    'o3': row['o3'],
                    'level': row['level'],
                    'primary_pollutant': row['primary_pollutant'],
                    'code': row['code']
                }
                print(f'{province}省{cityName}>> {info}')
        return

    if type == '8':
        data = item['result']['data']
        rows = data['rows']
        if rows:
            for row in rows[:30]:
                timepoint = row['timepoint']
                info = {
                    'aqi': row['aqi'],
                    'pm2.5': row['pm2_5'],
                    'pm10': row['pm10'],
                    'temp': row['temp'],
                    'humi': row['humi'],
                    'wse': row['wse']
                }
                print(f'{timepoint}>> {info}')
        return

    if type == '9':
        data = item['result']['data']
        rows = data['rows']
        if rows:
            for row in rows[:30]:
                cityName = row['city']
                info = {
                    'people': row['people'],
                    'gdp': row['gdp'],
                    'aqi': row['aqi']
                }
                print(f'{cityName}>> {info}')
        return


