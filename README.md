# 大连理工大学图书馆自动预约座位小程序

框架来自于[ShuaichiLi/DLUT-library-auto-reservation](https://github.com/ShuaichiLi/DLUT-library-auto-reservation)

## 特性
- 如果预约成功，程序会弹窗提示“预约xxx成功”
- 如果失败，则无弹窗

## 做出的修改
- 去掉了页面的滑动，当前可以精确定位一个座位（代码量直接大幅下降doge）

## 依赖项
- [Chromedriver](https://chromedriver.chromium.org/downloads) 记得下载对应版本，解压到```/driver```文件夹里
- [Python](https://www.python.org/downloads/) 
- selenium （推荐使用[pip](https://pip.pypa.io/en/stable/installation/)）
  - ```pip install -U selenium``` (For Linux)
  - ```py -m pip install -U selenium``` (For Windows)


- 不下依赖包用个der啊

  ![](files/dddd.jpg)

## 使用
### - ```py main.py``` 或者直接运行```run.bat```
- 通过修改```main.py```中```user_id```和```password```来设置账号密码
- 修改```room_id```字段选择对应房间，我只注释了令希的，平时不去博川
- 修改```favorSeats```字段来设定自己喜欢的座位（群）
  -座位号两边需要加' '，不可省略(str字符串)

## 未来（神tm未来）
- 可能以后会打包成程序
