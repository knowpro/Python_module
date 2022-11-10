setwd("C:\\DBDA\\Python\\R programming\\DS\\")
df=read.csv("cars2.csv")
df

getwd()

colnames(df)
names(df)


#-------------------------------------
summary(df)
str(df)

df$speed
attach(df)
speed
detach(df)

----------------------------------------
v<-1:10
ifelse(v%%2==0,"even","odd")

mean(v)
var(v)
sd(v)
  

log(10)
log10(45)
log2(23)

exp(2.302585)
exp(1.653213)
exp(4.523562)




