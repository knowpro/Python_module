#Conditional Statement
a<-readline("Enter no:")
a<-as.integer(a)
if(a>0)
{
  print("a is Positive")
}


a<- 13L
if(a%%2 ==0){
  print("even")
}else{
  print("odd")
}
  
a<- -13L
if(a>0){
if(a%%2 ==0){
  print("even")
}else if(a%%2==1){
  print("odd")
}
}else{
  print("No is Negative")
}



for(i in 1:5){
  print(i)
}

no<-1
while(no<=100){
  if(no%%2==1){
    print(no)
  }
  no=no+1
}

n<-10
repeat{
  print(n)
  if (n> 500){
    break
  } 
  n=n+5
}

no<-0
while(no<=10){
  no=no+1
  if(no==5){
    break
  }
 print(no)
}



no<-0
while(no<=10){
  no=no+1
  if(no==5){
    next
  }
  print(no)
}


a<-switch(2,
          "case1",
          "case2",
          "case3"
          )
a


a<-switch(5,
          "case1",
          "case2",
          "case3"
)
a

#----------------------------------------
#Functions

add<- function(a,b){
  print(a+b)
}
add(12,4)


add<- function(a,b){
  a+b
}
add(120,40)


add<- function(a,b){
  return(a+b)
}
add(10,10)


pow<- function(ba,pw){
  return(ba^pw)
}

pow(4,3)
ls()
save.image("C:\\DBDA\\Python\\R programming\\Day1\\test")


load("C:\\DBDA\\Python\\R programming\\Day1\\test")
rm(a)#remove 'a' element
rm(list=ls())#remove all element
