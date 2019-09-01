###读入数据
library(network)
library(ergm)
library("statnet")

##读取数据
data <- read.csv("D:/上市公司网络数据/fenlei/hebing8.csv")

data$流通市值.万元.[is.na(data$流通市值.万元.)] <- 0
##转化成为数据框
data <- as.data.frame(data)

juzhen <- read.table("D:/上市公司网络数据/fenlei/word_vector6.txt")

as.data.frame(juzhen)

mx <- as.matrix(juzhen)

sss<- dist(mx,p=2)
###做成网络S3文件,导入的是邻接矩阵的类型
n = network(mx, vertex.attr=NULL, vertex.attrnames=NULL, matrix.type="adjacency", directed=FALSE,encoding='GB2312')
summary(n) # 看一下网络的基本信息


###建立一个节点的数据框
library(intergraph)
library(network)

data$Id <- node$Id
node = data.frame(network.vertex.names(n), stringsAsFactors = F)  
names(node) = c("Id")


###合并二者
library(dplyr)
m <- left_join(node,data,by = "Id")



m$股东名称 <- as.character(m$股东名称)
m$行业 <- as.character(m$行业)

set.vertex.attribute(n,"股东名称",m$股东名称)

set.vertex.attribute(n,"数量变化",m$数量变化.万股.)

set.vertex.attribute(n,"流通市值",m$流通市值.万元.)

set.vertex.attribute(n,"分类",m$mark1)

set.vertex.attribute(n,"所投行业",m$行业)

set.vertex.attribute(n,"个体",m$个人)

set.vertex.attribute(n,"央企",m$央企)

set.vertex.attribute(n,"投行",m$投行)

set.vertex.attribute(n,"体量",m$筛选)

###设置节点属性和边属性


###将网络图文件保存为,换名字
jss3 <- saveRDS(n, "D:/上市公司网络数据/fenlei/n.rds1")
jss3 <- saveRDS(n, "D:/上市公司网络数据/fenlei/n.rds2")

hh <- readRDS("D:/上市公司网络数据/fenlei/n.rds1")
jj <- readRDS("D:/上市公司网络数据/fenlei/n.rds2")




###拟合ergm模型
model <- ergm(n~edges+nodecov("流通市值")+gwesp(fixed=T, cutoff=30)+
                nodecov("数量变化")+nodematch("个体")+nodematch("投行")+
                nodematch("央企")+nodemix("类别",base=4)+kstar(1)+degree(1:3))

model <- ergm(hh~edges)

model <- ergm(jj~edges+nodecov("数量变化")+
              nodecov("流通市值")+nodecov("体量")+nodemix("分类",base=4))

model <- ergm(hh~edges+gwdsp+nodemix("分类",base=4))


summary(model)


summary(jj)

summary(hh)
###进行模型的拟合优度测试，并且作图
fit= gof(model)
summary(fit)
par(mfrow=c(2,2))
plot(fit)

dist(hh,p=2)

class(hh)

