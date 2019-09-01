# -*- coding: utf-8 -*-
"""
Created on Wed May 22 21:19:23 2019

@author: Caiyunbin
"""

import pandas as pd
import numpy as np

##读入数据
data = pd.read_csv('D:/上市公司网络数据/fenlei/111.csv',encoding='utf-8')

data_a = pd.read_csv('D:/上市公司网络数据/xiaoshuju.csv',encoding='utf-8')

###个体——其他的网络
df1=data[data.Source.str.contains(r'^[\u4E00-\u9FA5]{2,3}$')| 
        data.Target.str.contains(r'^[\u4E00-\u9FA5]{2,3}$')]

###对于权重进行排序
df2=df1.sort_values(by="Weight",ascending=False)

###统计各个权重拥有的键值对情况
print(df2['Weight'].value_counts())

###个体-个体的投资网络
df3=data[data.Source.str.contains(r'^[\u4E00-\u9FA5]{2,3}$')&
         data.Target.str.contains(r'^[\u4E00-\u9FA5]{2,3}$')]

df4=df3.sort_values(by="Weight",ascending=False)

###最大的键值对
print(df4.iloc[0,:])

###统计各个数值的个数
print(df4['Weight'].value_counts())

import re

def func(a):
    if  re.match(r'^[\u4E00-\u9FA5]{2,3}$',a):
        return 3            ##表示个体户
    elif re.match(r'全国社保|中国|中央汇金|香港中央|华夏新经济|嘉实|南方消费动力|招商丰庆A|工银瑞信|南方基金|中欧|博时|大成|嘉实|广发|华夏|银华|易方达',a): 
        return 2            ##表示央企
    else:
        return 1            ##表示一般企业
    
data['mark1'] = data.apply(lambda x:func(x.股东名称),axis=1)

data['mark2'] = data.apply(lambda x:func(x.Target),axis=1)


def modify(a,b):
    if a==3 and b==3:
        return '个体-个体'
    elif (a==3 and b==2)|(a==2 and b==3):
        return '个体-央企'
    elif (a==3 and b==1)|(a==1 and b==3):
        return '个体-投行'
    elif a==2 and b==2:
        return '央企-央企'
    elif (a==2 and b==1)|(a==1 and b==2):
        return '央企-投行'
    else:
        return '投行-投行'
    
data['class'] = data.apply(lambda x:modify(x.mark1,x.mark2),axis=1)

data.to_csv("D:/上市公司网络数据/fenlei/jianshao66.csv",encoding='utf-8')

print(data['class'].value_counts())

print(data['Weight'].groupby(data['class']).count())

print(data['mark1'].value_counts())

print(data['mark2'].value_counts())

###关于定点的数据写入
data1 = pd.read_csv('D:/上市公司网络数据/yuanshi.csv',encoding='utf-8')

data1['Weight'] = data1.apply(lambda x:func(x.股东名称),axis=1)

print(data1['count'].value_counts())


###筛选六网
ge_ge = data.loc[data["class"] == "个体-个体",["Source","Target","Weight"]].sort_values(['Weight'],ascending=False)

ge_tou = data.loc[data["class"] == "个体-投行",["Source","Target","Weight"]].sort_values(['Weight'],ascending=False)

ge_yang = data.loc[data["class"] == "个体-央企",["Source","Target","Weight"]].sort_values(['Weight'],ascending=False)

tou_tou = data.loc[data["class"] == "投行-投行",["Source","Target","Weight"]].sort_values(['Weight'],ascending=False)

tou_yang = data.loc[data["class"] == "央企-投行",["Source","Target","Weight"]].sort_values(['Weight'],ascending=False)

yang_yang = data.loc[data["class"] == "央企-央企",["Source","Target","Weight"]].sort_values(['Weight'],ascending=False)



ge_ge = data.loc[data["class"] == "个体-个体",["Source","Target","Weight"]]

ge_tou = data.loc[data["class"] == "个体-投行",["Source","Target","Weight"]]

ge_yang = data.loc[data["class"] == "个体-央企",["Source","Target","Weight"]]

tou_tou = data.loc[data["class"] == "投行-投行",["Source","Target","Weight"]]

tou_yang = data.loc[data["class"] == "央企-投行",["Source","Target","Weight"]]

yang_yang = data.loc[data["class"] == "央企-央企",["Source","Target","Weight"]]

##写入文件
ge_ge.to_csv("D:/上市公司网络数据/6wang/ge_ge.csv",encoding="utf-8",index=False,header=True)
ge_tou.to_csv("D:/上市公司网络数据/6wang/ge_tou.csv",encoding="utf-8",index=False,header=True)
ge_yang.to_csv("D:/上市公司网络数据/6wang/ge_yang.csv",encoding="utf-8",index=False,header=True)
tou_tou.to_csv("D:/上市公司网络数据/6wang/tou_tou.csv",encoding="utf-8",index=False,header=True)
tou_yang.to_csv("D:/上市公司网络数据/6wang/tou_yang.csv",encoding="utf-8",index=False,header=True)
yang_yang.to_csv("D:/上市公司网络数据/6wang/yang_yang.csv",encoding="utf-8",index=False,header=True)

###增加一列
data = pd.read_csv('D:/上市公司网络数据/yuanshi.csv',encoding='utf-8')

import re

def func(a):
    if  re.match(r'^[\u4E00-\u9FA5]{2,3}$',a):
        return 3            ##表示个体户
    elif re.match(r'全国社保|中国|中央汇金|香港中央|华夏新经济|嘉实|南方消费动力|招商丰庆A|工银瑞信|南方基金|中欧|博时|大成|嘉实|广发|华夏|银华|易方达',a): 
        return 2            ##表示央企
    else:
        return 1            ##表示一般企业
    
data['mark1'] = data.apply(lambda x:func(x.股东名称),axis=1)

data.to_csv("D:/上市公司网络数据/zengjia_nodes.csv",encoding="utf-8",index=False,header=True)
