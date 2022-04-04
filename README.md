# 大连理工大学图书馆自动预约座位小程序

[![Build status (GitHub)](https://img.shields.io/github/workflow/status/qhy040404/DLUT-library-auto-reservation/Compile-CI/master?label=Compile&logo=github&cacheSeconds=600)](https://github.com/qhy040404/DLUT-library-auto-reservation/actions)
[![CodeFactor](https://www.codefactor.io/repository/github/qhy040404/dlut-library-auto-reservation/badge)](https://www.codefactor.io/repository/github/qhy040404/dlut-library-auto-reservation)
[![Github last commit date](https://img.shields.io/github/last-commit/qhy040404/DLUT-library-auto-reservation.svg?label=Updated&logo=github&cacheSeconds=600)](https://github.com/qhy040404/DLUT-library-auto-reservation/commits)
[![License](https://img.shields.io/github/license/qhy040404/DLUT-library-auto-reservation.svg?label=License&logo=github&cacheSeconds=2592000)](https://github.com/qhy040404/DLUT-library-auto-reservation/blob/master/LICENSE)

框架来自于[ShuaichiLi/DLUT-library-auto-reservation](https://github.com/ShuaichiLi/DLUT-library-auto-reservation)

## 特性
- 预约成功后无弹窗，以防止程序在弹窗后等待点击而持续运行
- 可以通过邮件推送预约结果

## 做出的修改
- 去掉了页面的滑动，当前可以精确定位一个座位（代码量直接大幅下降doge）

## 依赖项
- 直接运行源程序请完整安装下述依赖包
  - [Chromedriver](https://chromedriver.chromium.org/downloads) 记得下载对应版本，解压到```/driver```文件夹里
  - [Python](https://www.python.org/downloads/) 
  - selenium （推荐使用[pip](https://pip.pypa.io/en/stable/installation/)）
    - ```pip install -U selenium``` (For Linux)
    - ```py -m pip install -U selenium``` (For Windows)
  - 不下依赖包用个der啊
- 如果使用打包后版本，请确认Chromedriver与电脑上的Chrome版本相对应
  - 编译进安装包内的Chromedriver对应Chrome99，如版本不同请到[此处](https://chromedriver.chromium.org/downloads)自行下载对应版本
  - 或者下载最新版[Chrome](https://www.google.cn/chrome)

## 使用
- 直接运行源程序
  - 运行配置生成器来生成配置文件
  - 生成器需要管理员权限才能在安装目录生成配置文件
  - 配置生成器可以到[这里](https://github.com/qhy040404/Library-reservation-configGenerator/releases)下载独立文件，拷贝至```.py```源文件目录运行
- 运行打包后的程序
  - 在[Releases](https://github.com/qhy040404/DLUT-library-auto-reservation/releases)中下载最新版安装使用即可
  - 桌面上会自动创建主程序和配置生成器的快捷方式

## 链接
- [ShuaichiLi/DLUT-library-auto-reservation](https://github.com/ShuaichiLi/DLUT-library-auto-reservation)
- [配置生成器](https://github.com/qhy040404/Library-reservation-configGenerator)