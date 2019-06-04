真气网全国空气质量爬虫
======================

反爬手段：API的post请求参数为js加密，且返回的response也是经过加密的。

如下图：

![image](https://github.com/xzh0723/ZhenQiAQI/blob/master/view/param.png)

![image](https://github.com/xzh0723/ZhenQiAQI/blob/master/view/data.png)

这段的js其实是比较好找的，常用的js调试手段就可以找到，js代码也不需要改，copy下来直接就可以运行，其实还是比较简单的，就是代码量有点多，看起来有点厉害，又是AES加密、又是DES加密、又是Base64加密，其实是纸老虎。。  

之后打算去学GUI界面，把这个爬虫做成界面，然后再做一些数据分析的图。

运行效果
============
![image](https://github.com/xzh0723/ZhenQiAQI/blob/master/view/view.png)
