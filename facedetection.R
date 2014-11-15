library("ggplot2")
library("devtools")
library("plotrix")
#read File
data<-read.csv('test.csv')
a<-table(data$NoOffaces)
a
qplot(data$NoOffaces)
#different visualisations
#1. Simple qplot
#2. Pie Chart
#3. 3D pie chart

cols <- c("grey90","grey50","black","grey30","white","grey70","grey50")
percentlabels<- round(100*a/sum(a), 1)
pielabels<- paste(percentlabels, "%", sep="")
pie(a,radius=1.0, main="My First Piechart", col=cols, labels=pielabels, cex=0.8)
pie3D(a, radius=1.5)

#installing rHighcharts from gir=thub
install_github("rHighcharts", "metagraf")

mat2 <- rbind(as.numeric(names(a)),a)
mat2
rownames(mat2) <- c("Faces", "Count")
mat2
mat2[1, ]
mat2[2, ]

#Using rHighchart which is a javascript with r visulisation

require(rHighcharts)
b <- rHighcharts:::Chart$new()
b$title(text = "Faces")

#Hardcore values
b$data(x = c("0 Faces","1 Face","2 Faces","3 Faces","4 Faces","5 Faces","6 Faces","7 Faces","8 Faces","9 Faces","10 Faces","14 Faces","15 Faces","19 Faces"),y = c(448,375,104,33,16,7,4,2,2,3,1,3,1,1), type = "pie", name = "Count")
b

