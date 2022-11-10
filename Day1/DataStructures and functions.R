v<-c(1,2,3,4,5)
v
v1<-c("a","b","c","d")
v1

v<-c(1,2,3,4,5,'x')
v

v<-1:20
v

v<-10:1
v

v<-seq(1,10)
v

v<-seq(1,10,2) #step
v

v<-seq(1,10,length.out=7)
v

v<-rep(1:2,times=3)
v

v<-rep(1:2,3)
v


v<-rep(1:2,each=3)
v

min(v)
max(v)
length(v)
mean(v)
unique(v)
sort(v)
rev(v)
table(v)

append(v,10)
v

#----------------------------------------

lst<-list(1,3.5,TRUE,c(12,34))

lst

lst[4]

lst<-list(a=1,b=3.5,c=TRUE,d=c(12,34))

lst

lst$d[2]

lst[4][1,2]

#------------------------

v<-c("Pass","Fail","Pass","Fail","Pass","Fail")
f<-factor(v)
f

f<-factor(v,levels = c("Fail", "Pass","Absent"))
f

#------------------------------------
m<-matrix(10,3,4)
m

m<-matrix(c(1,2,3,4,5,6),2,3)
m

m<-matrix(c(1,2,3,4,5,6),2,3,byrow = TRUE)
m


a<-1:5
b<-6:10
c<-11:15

cbind(a,b,c)

rbind(a,b,c)

#-----------------------------------------

a<-array(dim=c(5))
a

a<-array(1:10,dim=c(2,5))
a


a<-array(1:20,dim=c(2,5,2))
a
#---------------------------

nm<-c("ravi","kishor","rishi")
age<-c(34,56,45)
adhar<-c(1234,345,678)

df=data.frame(nm,age,adhar)
df

df=read.csv("C:\\DBDA\\Python\\R programming\\DS\\cars2.csv")
df

