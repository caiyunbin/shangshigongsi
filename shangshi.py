# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import networkx as nx
import codecs
import matplotlib.pyplot as plt

data = pd.read_csv("D:/上市公司网络数据/yuanshi.csv",encoding="UTF-8")
data1 = pd.read_csv("D:/上市公司网络数据/two.csv",encoding="UTF-8")

data2=data1.drop('name',axis=1)

data3=data2.drop([0])

a=data2.as_matrix()

b=data1.values

result=np.dot(a,a.T)

print(data[:4])

###按照教程
name=[]
for n in data[u'股东名称']:
    name.append(n)
print(name[0])

name1=[]
for n in data[u'hao']:
    name1.append(n)
    
a=np.zeros([2,3])

print(a)

print(len(name))

word_vector = np.zeros([len(name1),len(name1)])

##计算共现矩阵
i=0
while i<len(name1):
    company1 = data[u'股票简称'][i]
    j = i + 1
    while j<len(name1):
        company2 = data[u'股票简称'][j]
        if company1==company2: 
            word_vector[i][j] += 1
            word_vector[j][i] += 1
        j = j + 1   
    i = i + 1
print(word_vector)
np_data = np.array(word_vector)  #矩阵写入文件
pd_data = pd.DataFrame(np_data)
pd_data.to_csv('D:/上市公司网络数据/result1.csv')

name2=data['hao'].astype(str)
###写一个三列矩阵
words = codecs.open("word_node10.txt", "a+", "utf-8")
i = 0
while i<len(name2):  #len(name)
    corp1 = name2[i]
    j = i + 1
    while j<len(name2):
        corp2 = name2[j]
        #判断学生是否共现 共现词频不为0则加入
        if word_vector[i][j]>0:
            words.write(corp1 + "," + corp2 + "," 
                + str(word_vector[i][j]) + "\r\n")
        j = j + 1
    i = i + 1
words.close()

###将txt文件转化成csv
data_txt=np.loadtxt('word_node.txt',encoding="utf-8")
data_txtDF=pd.DataFrame(data_txt)
data_txtDF.to_csv('data_result.csv',index=False)

lines = open('word_node10.txt',encoding='utf-8').readlines()

fp2 = open('test11.csv','w')  
for s in lines:
    fp2.write(s)

import os
os.getcwd()

a = []
f = codecs.open('D:/上市公司网络数据/新建文件夹/word_node60.txt','r','utf-8')
line = f.readline()
print(line)

i = 0
A = []
B = []
while line!="":
    a.append(line.split(','))   #保存文件是以空格分离的
    print(a[i][0],a[i][1])
    A.append(a[i][0])
    B.append(a[i][1])
    i = i + 1
    line = f.readline()
elem_dic = tuple(zip(A,B)) 
print(type(elem_dic))
print(list(elem_dic))
f.close()

plt.rcParams['font.sans-serif'] = ['SimHei']   
plt.rcParams['font.family']='sans-serif'

G = nx.Graph()
G.add_edges_from(list(elem_dic))

pos=nx.random_layout(G)
nx.draw_networkx_nodes(G, pos, alpha=0.2,node_size=120)


