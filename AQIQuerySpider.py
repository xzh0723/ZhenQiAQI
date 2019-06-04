import requests
import execjs
import json
from TypeProcessor import typeProcess
from ParseProcessor import parseProcess

class AqiQuerySpider():

    def __init__(self, method, object_, API):
        self.method = method
        self.object_ = object_
        self.API = API

    def get_param(self):
        """
        获取请求API所需的加密参数：两个不同API的加密参数不同
        （1）https://www.aqistudy.cn/apinew/aqistudyapi.php ： d 参数,  JS文件: apiStudyJs
        （2）https://www.zq12369.com/api/newzhenqiapi.php ： param 参数,  JS文件: newZhenqiJs
        （3）https://m.zq12369.com/api/newzhenqiapi.php ： param 参数,  JS文件: newZhenqiJs
        :return:
        """
        if self.API == 'https://www.aqistudy.cn/apinew/aqistudyapi.php':
            with open('aqiStudyJs.js', 'rb') as f:
                js = f.read().decode('utf-8')
            ctx = execjs.compile(js)
            param = ctx.call('getParam', self.method, self.object_)
        else:
            with open('newZhenqiJs.js', 'rb') as f:
                js = f.read().decode('utf-8')
            ctx = execjs.compile(js)
            param = ctx.call('getParam', self.method, self.object_)
        return param

    def reqAPI(self, param):
        """
        请求API获取数据
        对于三个不同的API，其中两个API请求方式与js加密数据解密完全一致，相当于需要两种方法进行请求和加解密
        这里给其中一致方法加一个标志，即返回字典，以便后面做判断
        :return:
        """
        if self.API == 'https://www.aqistudy.cn/apinew/aqistudyapi.php':
            response = requests.post(self.API, data={'d': param})
            encryptData = response.text
        else:
            response = requests.post(self.API, data={'param': param})
            encryptData = {'zhenqi': response.text}
        print('=====' * 100)
        print(f'返回的加密数据：{encryptData}')
        print('=====' * 100)
        return encryptData

    def decryptData(self, data):
        """
        解密获取的数据
        :param response:
        :return:
        """
        if isinstance(data, dict):
            with open('newZhenqiJs.js', 'rb') as f:
                js = f.read().decode('utf-8')
            ctx = execjs.compile(js)
            result = ctx.call('decodeData', data['zhenqi'])
        else:
            with open('aqiStudyJs.js', 'rb') as f:
                js = f.read().decode('utf-8')
            ctx = execjs.compile(js)
            result = ctx.call('decodeData', data)
        return result

    def run(self):
        """
        主函数运行
        :return:
        """
        # 获取加密参数
        param = self.get_param()
        # 利用获取的加密参数请求API
        encryptData = self.reqAPI(param)
        # 对请求API获取的加密数据进行解密
        result = self.decryptData(encryptData)
        decryptData = json.loads(result)
        print(f'解密后的数据：{decryptData}')
        print('=====' * 100)
        return decryptData

if __name__ == '__main__':
    while True:
        print(f'我们的服务类型有：实时监控(0) 监测曲线(1) 全国分布(2) 省份分布(3) 实时168城市排名(4) 城市比较(5) 时段统计(6) 统计排名(7) 天气关联(8) 经济关联(9)')
        print('=====' * 100)
        type_ = input('请输入您要查询的类型(对应括号中的数字)>> ')
        print('=====' * 100)
        method, object_, API = typeProcess(type_)
        if method:
            # 启动爬虫获取正常数据
            spider = AqiQuerySpider(method, object_, API)
            decryptData = spider.run()
            # 解析数据
            parseProcess(type_, decryptData)
            print('=====' * 100)

            flag = input('如需继续查询请按 1 继续，否则任意键结束程序')
            print('=====' * 100)
            if flag != '1':
                break
        else:
            continue