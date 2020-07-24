# R is for Everyone
# Commands

#Basics of R
1+1
1+2+3
3*7*2
4/2
4/3
4*6+5
(4*6)+5
4*(6+5)
x<-2
x
y = 5
y
3-> z
z
a<- b <- 7
a
b
assign("j",4)
j
rm(j)
j
theVariable <- 17
theVariable
THEVARIABLE
class(x)
is.numeric(x)
i <-5L
i
is.integer(i)
is.numeric(i)
class(4L)
class(2.8)
4L * 2.8
class(4L * 2.8)
class(5L)
class(2L)
5L/2L
class (5L/2L)
x<- "data"
x
y<- factor ("data")
y
nchar(x)
nchar("hello")
nchar (3)
nchar (452)
nchar (y)
date1 <- as.Date("2012-06-28")
date1
class(date1)
as.numeric(date1)
date2<- as.POSIXct("2012-06-28 17:42")
date2
class(date2)
as.numeric(date2)
class(date1)
class(as.numeric(date1))
TRUE * 5
FALSE * 5
k<- TRUE
class(k)
is.logical("k")
TRUE
T
class(T)
T<- 7 
T
class(T)
2 == 3
2 != 3
2 < 3
2 <= 3
2 > 3
2 >= 3
"data" == "stats"
"data" < "stats"
x<- c(1,2,3,4,5,6,7,8,9,10)
x
x * 3
x
x / 3
x
x + 2
x
x -2
x
x / 4
x
x * 4
x
x ^ 2
x
sqrt(x)
1:10
10:1
-2:3
5:-7
x<- 1:10
y<- -5:4
x
y
x+y
x-y
x*y
x/y
x
y
x^y
length(x)
length(y)
length(x+y)
x
x+c(1,2)
x+c(1,2,3)
x<=5
x
y
x>y
x<y
x<10:1
y<- -4:5
all(x<y)
any(x<y)
q<- c("Hockey", "Football", "Baseball", "Curling", "Rugby",
"Lacrosse", "Basketball", "Tennis", "Cricket", "Soccer")
q
nchar(q)
y
nchar(y)
x<- 10:1
x
x[1]
x[1:2]
x[c(1,4)]
c(One="a", Two="b", Last="r")
w<- 1:3
names(w)<-c("a","b","c")
w
q2<- c(q, "Hockey", "Lacrosse", "Water",
"Polo", "Hockey", "Lacrosse")
q
q2
q2Factor<- as.factor(q2)
q2Factor
as.numeric(q2Factor)
factor(x=c("High School", "College", "Masters", "Doctorate"),
levels=c("High School", "College", "Masters", "Doctorate"),
ordered=TRUE)
mean(x)
?`+`
?`*`
?`==`
?apropos
apropos("mea")
z<-c(1,2,NA,8,3,NA,3)
z
is.na(z)
zChar<-c("Hockey",NA,"Lacrosse")
zChar
is.na(zChar)
mean(z)
z
mean(z,na.rm=TRUE)
sum(z,na.rm=TRUE)
min(z,na.rm=TRUE)
max(z,na.rm=TRUE)
var(z,na.rm=TRUE)
sd(z,na.rm=TRUE)
z<- c(1,NULL,3)
z
d<-NULL
is.null(d)
is.null(7)
