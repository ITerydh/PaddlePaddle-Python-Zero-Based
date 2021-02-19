# PaddlePaddle-Python-Zero-Based
百度飞桨领航团零基础Python入门
---

![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/1.png)

[TOC]

Table of Contents
=================

   * [PaddlePaddle-Python-Zero-Based](#PaddlePaddle-Python-Zero-Based)
      * [百度飞桨领航团零基础Python入门](#百度飞桨领航团零基础Python入门)
   * [课程框架](#课程框架)
   * [一、python环境配置及入门](#一、python环境配置及入门)
      * [1.配置](#1.配置)
      * [2.入门](#2.入门)
         * [第一个程序](#第一个程序)
         * [基本数据类型](#基本数据类型)
         * [基本运算符](#基本运算符)
         * [起名法则](#起名法则)
         * [数据类型间相互转换](#数据类型间相互转换)
         * [组合数据类型](#组合数据类型)
            * [list](#list)
            * [元组 tuple](#元组 tuple)
         * [可变对象 不可变对象](#可变对象 不可变对象)
         * [字典dict](#字典dict)
         * [集合 set](#集合 set)
         * [if语句](#if语句)
         * [循环语句](#循环语句)
         * [break continue pass](#break continue pass)
   * [二、python编程基础](#二、python编程基础)
      * [字符串进阶](#字符串进阶)
         * [字符串索引、切片](#字符串索引、切片)
         * [字符串常用函数](#字符串常用函数#)
      * [list进阶](#list进阶)
         * [list索引、切片](#list索引、切片)
         * [list常用函数](#list常用函数)
            * [列表生成式](#列表生成式)
      * [生成器](#生成器)
      * [练习 斐波那契数列](#练习 斐波那契数列#)
      * [异常处理](#异常处理)
   * [三、Python函数基础](#三、Python函数基础)
      * [定义一个函数并使用](#定义一个函数并使用#)
      * [参数传递](#参数传递)
         * [位置参数](#位置参数)
         * [缺省参数](#缺省参数)
         * [可变参数](#可变参数)
         * [关键字参数](#关键字参数)
         * [命名关键字参数](#命名关键字参数)
      * [参数的组合](#参数的组合)
      * [lambda匿名函数](#lambda匿名函数)
      * [高阶函数](#高阶函数)
         * [print](#print)
         * [sorted](#sorted)
      * [模块](#模块)
      * [大作业一](#大作业一)
   * [面向对象](#面向对象)
      * [大作业二](#大作业二)
      * [大作业三](#大作业三)
      * [大作业四](#大作业四)
   * [总结](#总结)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc)



# 课程框架

一句话！一篇文章学会Python!


# 一、python环境配置及入门
## 1.配置
方法一
直接安装python本体（不推荐） 
下载地址： https://www.python.org/downloads/ 
方法二
Anaconda（强烈推荐！） 
下载地址 https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/
方法三：
百度AI Studio（强烈推荐！） 访问地址 https://aistudio.baidu.com/
为了方便管理，后续作业在百度AI Studio上完成。为了和教学版本一致，本地环境最好下载python3.7版本（anaconda：2019年7月版本，注意下载anaconda3）

**这软件安装都不再多说了，相信大家都稳得一笔了！**

## 2.入门
全文以anaconda作为演示，如果你不想用这个，其他二者是完全一样的。

![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/2.png)
因为入门，打开这个即可，其他环境都不需要管。

### 第一个程序
看看大概有个了解即可，不必深究，等文章看完一遍再看第二遍，你一定会豁然开朗
![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/3.png)
### 基本数据类型
整数：int
浮点数：也就是小数float
字符串：

```python
字符串是以单引号'或双引号"括起来的任意文本
'this is a string'
"yes"
'爸爸说："今天我做饭"'
"爸爸说：\"今天我做饭\""
len('hello world!')
```

![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/4.png)
布尔值：True False
![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/5.png)
空值：None
空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值


### 基本运算符
![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/6.png)
变量赋值：（学过其他语言一笔带过即可，没学过一定要一个一个试试）
![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/7.png)
### 起名法则

简单地理解，标识符就是一个名字，就好像我们每个人都有属于自己的名字，它的主要作用就是作为变量、函数、类、模块以及其他对象的名称

Python 中标识符的命名不是随意的，而是要遵守一定的命令规则，比如说：

标识符是由字符（A~Z 和 a~z）、下划线和数字组成，但第一个字符不能是数字。 标识符不能和 Python 中的保留字相同。 Python中的标识符中，不能包含空格、@、% 以及 $ 等特殊字符。 在 Python 中，标识符中的字母是严格区分大小写的

简单来说，你别护理呼哨的就行了，符号啥的你不用就完事了

###  数据类型间相互转换
![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/8.png)
### 组合数据类型
#### list
list是一种有序的集合，可以随时添加和删除其中的元素。
![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/9.png)
#### 元组 tuple
另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/10.png)
### 可变对象 不可变对象
可变对象：list dict set

不可变对象：tuple string int float bool

### 字典dict
Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。

![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/11.png)
### 集合 set
set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。

![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/12.png)
### if语句
![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/13.png)
此外注意，新手必犯的错误！！！ 编程语言中==才是判断是否等于，一个=是赋值。
![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/14.png)
### 循环语句
![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/15.png)
复杂一点的用法
![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/16.png)
### break continue pass
如果希望在中间离开循环，也就是 f or 循环结束重复之前，或者 while 循环找到结束条件之 前。有两种⽅式来做到：
1. 使⽤ break 语句来完全终⽌循环。
2. 使⽤ continue 语句直接跳到循环的下⼀次迭代。
  ![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/17.png)
  ![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/18.png)
  ![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/19.png)
# 二、python编程基础
## 1.字符串进阶
### 字符串索引、切片
![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/20.png)
![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/21.png)
小应用
![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/22.png)
### 字符串常用函数
count 计数功能
显示自定字符在字符串当中的个数
![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/23.png)
find 查找功能
返回从左第一个指定字符的索引，找不到返回-1

index 查找
返回从左第一个指定字符的索引，找不到报错
![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/24.png)
![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/25.png)
split 字符串的拆分
![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/26.png)
字符串的替换
![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/27.png)
字符串标准化
默认去除两边的空格、换行符之类的，去除内容可以指定
![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/28.png)
字符串的变形
![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/29.png)
字符串的格式化输出 ☆
![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/30.png)
## list进阶
### list索引、切片
![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/31.png)
### list常用函数
添加新的元素
![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/32.png)
count 计数 和 index查找
![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/33.png)
删除元素
![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/34.png)
#### 列表生成式
![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/35.png)

## 生成器
通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
（大白话：不会直接运行完）
![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/36.png)
## 练习 斐波那契数列
![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/37.png)
## 异常处理
![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/38.png)
# 三、Python函数基础
定义：
函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。

函数能提高应用的模块性，和代码的重复利用率。你已经知道Python提供了许多内建函数，比如print()。但你也可以自己创建函数，这被叫做用户自定义函数。

函数代码块以 def 关键词开头，后接函数标识符名称和圆括号()。
任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。
函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
函数内容以冒号起始，并且缩进。
return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。

## 定义一个函数并使用
这个函数用来打印名字并return了dict的值
![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/39.png)
![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/40.png)
## 参数传递
### 位置参数
位置参数是最简单的一种函数调用的方式。位置参数须以正确的顺序传入函数、数量必须和声明时的一样。
![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/41.png)

### 缺省参数
调用函数时，缺省参数的值如果没有传入，则被认为是默认值。
![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/42.png)
### 可变参数
顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。
![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/43.png)
### 关键字参数
关键字参数允许你传入0个或任意个含参数名的参数，这些参数在自动组装为一个dict。
![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/44.png)
### 命名关键字参数
如果要限制关键字参数的名字，就可以用命名关键字参数
![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/45.png)
## 参数的组合
在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/46.png)
## lambda匿名函数
python 使用 lambda 来创建匿名函数。

lambda 只是一个表达式，函数体比 def 简单很多。

lambda 的主体是一个表达式，而不是一个代码块。仅仅能在 lambda 表达式中封装有限的逻辑进去。

lambda 函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。

虽然 lambda 函数看起来只能写一行，却不等同于 C 或 C++ 的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。

**我的理解（就给lambda当成特殊符号 ，看见他就是函数的内容要开始写了，冒号前是输入的参数，冒号后是输出的东西，这一个整块就是 一个函数，包括lambda字母）如下，是不是很清楚了**
![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/47.png)
## 高阶函数
### print
就不说了
### sorted
![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/48.png)
## 模块
如下图 time模块
代码第二行是让程序睡眠一秒，第一行和第三行是得到当前的时间
时间是秒为单位，起点是1970.01.01，所以第一行time不是0第三行不是1
![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/49.png)
安装/卸载第三方模块
pip install / uninstall
例如：打开cmd(anacondade启动选择第一个打开)
![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/50.png)
绿色的第一个选项就是了（图中后两个为我本人的学习环境，你们可以忽略）
![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/51.png)
## 大作业一
统计英语6级试题中所有单词的词频，并返回一个如下样式的字典

{'and':100,'abandon':5}
文本内容自行百度一段英文文章即可。
![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/52.png)
直接上本人的代码：
![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/53.png)
狡辩：没有用到 re模块，觉得不用实现也挺简单的（实际上没去学re正则表达式hhh）



# 面向对象
## 大作业二
通过前面的理解学习，基础的代码编写一定可以了，下面才是真正的进阶
直接 上代码，自行理解，并非最优代码，仅供学习参考
1.首先放入数据文本
![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/54.png)
内容分别为：自行写个txt放进去就行了
```python
loren,2011-11-3,270,3.59,4.11,3:11,3:23,4-10,3-23,4:10,4.21,4-21
mark,2010-2-4,300,3.59,3.11,3:11,3:23,4-10,4-23,4:10,4.21,4-21
```
作业要求：读取 上述文本，并将第三个数字后面的数据处理为3.59一样的类型数字，输出最大的三个数，Loren和Mark分别为Rugby对象和OtherAthlete对象，输出样例如下：

```bash
loren
2011-11-3
270
['3.11', '3.23', '3.59']
mark
2010-2-4
300
['3.11', '3.11', '3.23']
```

上代码！！！！
![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/55.png)
![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/56.png)
![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/57.png)
over，就不给你源码，气不气，自己练去吧！

## 大作业三
数据如下：

stu1.txt 孙同学,2020-5-21,20,'男',77,56,77,76,92,58,-91,84,69,-91
stu2.txt 赵同学,2020-11-3,24,'女',65,68,72,95,-81,71,86,91,57,91
stu3.txt 王同学,2021-8-7,25,'男',87,78,90,-76,88,47,100,65,69,100 
stu4.txt 李同学,2021-8-10,29,'男',92,54,85,71,-91,68,77,68,95,95

定义Student类，包括name、dob、age、gender和score属性，包括top3方法用来返回学生的最大的3个成绩（可重复）、sanitize方法用来将负的分数变为正的分数，负的分数可能是输入错误。声明stu_list对象组数用于存储所有的学生对象。最后输出所有的学生信息包括姓名、生日、年龄、性别、最高的3个分数。

第一题的输出结果如下，供参考：
![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/58.png)
这次不逼逼了，直接上代码 ：
![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/59.png)
## 大作业四
数据格式如下：

stu5.txt 特长同学,2020-10-5,20,'男',180,87,98,77,76,92,58,-76,84,69,-47
stu6.txt 特长同学,2020-10-6,20,'女',230,76,48,82,88,92,58,-91,84,69,-68

定义Spostudent、Artstudent为Student的子类，在子类的属性里面新增了spe为特长分数。Spostudent包括的top3方法返回的是最低的3个得分（可重复），Artstudent包括top3方法返回的是最高的3个得分（可重复），最后使用多态的方式输出2个特长同学的姓名、生日、年龄、性别、分数、特长分。

第二题的输出结果如下，供参考：
![在这里插入图片描述](https://github.com/ITerydh/PaddlePaddle-Python-Zero-Based/blob/main/asserts/60.png)
在作业二的基础上扩展如下代码：
![在这里插入图片描述](61.png)
over！到此为止，Python 你已经入门！


# 总结
<font color=#999AAA >感谢百度飞桨的这次免费公开课。老师讲的都很清晰耐心，本人有其他编程语言的底子，所以听起来会超级上手，可能编写的代码还是不够完美，但是足矣完成要求，本篇内容代码可以加私信本人csdn获取（不定期查看私信）。
