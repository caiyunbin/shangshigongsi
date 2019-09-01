library(network)
library(ergm)
library("statnet")


a <- read.csv("D:/上市公司网络数据/fenlei/hebing8.csv", encoding="UTF-8")

b <- read.csv("D:/上市公司网络数据/fenlei/zengjia_nodes.csv", encoding="Gb2312")

c <- read.csv("D:/上市公司网络数据/fenlei/zengjia2.csv", encoding="Gb2312")




##陈老师的文章
library(intergraph)
library(network)
library(igraph)

m1 <- as.matrix(a)

m2 <- m1[,c(1,2)]

n1 <- graph.edgelist(m2)


tie_other = intergraph:::as.matrix.igraph(n1, matrix.type='edgelist')
degree_other = igraph::degree(tie_other)
####
b1 <- as.data.frame(b)
  
cc <- ergm(n~edges)
summary(cc)

a[,1] = as.character(a[,1])　
a[,2] = as.character(a[,2])

n = network(a, vertex.attr=NULL, vertex.attrnames=NULL, matrix.type="edgelist", directed=FALSE,encoding='GB2312')
summary(n) # 看一下网络的基本信息

node = data.frame(network.vertex.names(n), stringsAsFactors = F)  
names(node) = c("Id")



library(dplyr)
m <- left_join(node,b1,by = "Id")

set.vertex.attribute(n,"个体",m$个体)

set.vertex.attribute(n,"央企",m$央企)

set.vertex.attribute(n,"投行",m$投行)

set.vertex.attribute(n,"数量变化",m$数量变化)

set.vertex.attribute(n,"流通市值",m$流通市值)

set.vertex.attribute(n,"类别",m$mark1)

set.edge.attribute(n,"个体-个体",c$个体.个体)

set.edge.attribute(n,"个体-央企",c$个体.央企)

set.edge.attribute(n,"个体-投行",c$个体.投行)

set.edge.attribute(n,"投行-投行",c$投行.投行)

set.edge.attribute(n,"央企-投行",c$央企.投行)

set.edge.attribute(n,"央企-央企",c$央企.央企)

set.edge.attribute(n,"Weight",c$Weight)

c$Weight <- as.numeric(c$Weight)
set.edge.value(n,"Weight",c$Weight)

delete.vertex.attribute(n,"流通市值")
summary(n)

model <- ergm(n~edges+nodecov("流通市值")+gwesp(fixed=T, cutoff=30)+
                nodecov("数量变化")+nodematch("个体")+nodematch("投行")+
                nodematch("央企")+nodemix("类别",base=4)+kstar(1)+degree(1:3))

model <- ergm(n~edges+dsp(2))        ##（1投2央3个） 
summary(model)

range(m$数量变化)

?ergm()

help(gwesp)
?mm


####模型拟合优度
fit= gof(model)
summary(fit)
par(mfrow=c(2,2))
plot(fit)

help(gof)
