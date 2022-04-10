# 大连理工大学图书馆自动预约座位小程序

[![Build status (GitHub)](https://img.shields.io/github/workflow/status/qhy040404/DLUT-library-auto-reservation/Compile-and-Test-CI/master?label=Compile&logo=github&cacheSeconds=600)](https://github.com/qhy040404/DLUT-library-auto-reservation/actions)
[![CodeFactor](https://www.codefactor.io/repository/github/qhy040404/dlut-library-auto-reservation/badge)](https://www.codefactor.io/repository/github/qhy040404/dlut-library-auto-reservation)
[![Github last commit date](https://img.shields.io/github/last-commit/qhy040404/DLUT-library-auto-reservation.svg?label=Updated&logo=github&cacheSeconds=600)](https://github.com/qhy040404/DLUT-library-auto-reservation/commits)
[![License](https://img.shields.io/github/license/qhy040404/DLUT-library-auto-reservation.svg?label=License&logo=github&cacheSeconds=2592000)](https://github.com/qhy040404/DLUT-library-auto-reservation/blob/master/LICENSE)

![GitHub top language](https://img.shields.io/github/languages/top/qhy040404/DLUT-library-auto-reservation)

# 2nd Generation
- 重写了整体架构
- 弃用selenium提供的webdriver方式，改用requests，大大减少了预约所需的时间
- 登录模块使用了[BeautyYuYanli/DLUT-login](https://github.com/BeautyYuYanli/DLUT-login)

## 特性
- 命令行界面回归，可以查看log
- 可通过邮件推送预约结果，以及预约失败原因（[错误码](ERRORCODE)）

## 依赖项
- [Python](https://www.python.org/downloads/) 
- requests （推荐使用[pip](https://pip.pypa.io/en/stable/installation/)）
  - ```pip install -U requests``` (For Linux)
  - ```py -m pip install -U requests``` (For Windows)
- 不下依赖包用个der啊

## 使用
- 直接运行源程序
  - 运行配置生成器来生成配置文件
  - 配置生成器可以到[这里](https://github.com/qhy040404/Library-reservation-configGenerator/releases)下载独立文件，拷贝至```.py```源文件目录运行
- 运行打包后的程序
  - 在[Releases](https://github.com/qhy040404/DLUT-library-auto-reservation/releases)中下载最新版安装使用即可
  - 桌面上会自动创建主程序和配置生成器的快捷方式

## 链接
- [ShuaichiLi/DLUT-library-auto-reservation](https://github.com/ShuaichiLi/DLUT-library-auto-reservation)
- [BeautyYuYanli/DLUT-login](https://github.com/BeautyYuYanli/DLUT-login)
- [配置生成器](https://github.com/qhy040404/Library-reservation-configGenerator)
- [体育馆预约](https://github.com/qhy040404/DLUT-gym-auto-reservation)
