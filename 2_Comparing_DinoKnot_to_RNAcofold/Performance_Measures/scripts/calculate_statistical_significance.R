## Load Libraries 
library(tidyverse)
library(dplyr)
library(boot)
library(perm)

# Set permutation test control used in all tests below

PC <- permControl(tsmethod="abs",nmc=10000)

## Set function

samplemean <- function(x,i){
  return (mean(x[i]))
}

##### MFE STRUCTURE ###########

#### DINOKNOT
dinoknot_calcs <- read.csv("~/dinoknot_TPR_PPV_MCC_calculations.csv") # read in file of snoRNA and sRNA performance metrics


DinoKnot_srna <- dinoknot_calcs %>% filter(str_detect(rna_type,"srna"))

DinoKnot_snorna <- dinoknot_calcs %>% filter(str_detect(rna_type, "snorna"))


#### RNAcofold

RNAcofold_snorna <- read_csv("~/RNAcofold_snorna_TPR_MCC_PPV.csv") # read in file of performance metrics

RNAcofold_srna <- read_csv("~/RNAcofold_srna_TPP_MCC_PPV.csv")


#######################################################SRNA

###################################### PPV

Dinoknot <- DinoKnot_srna$PPV
RNAcofold <- RNAcofold_srna$PPV

### PERMUTATION TEST

#Dinoknot AND #RNAcofold

permTS(Dinoknot,RNAcofold,alternative="two.sided",method="exact.mc",control=PC) 



## BOOT STRAPPING 

#Dinoknot

b1 = boot(Dinoknot,samplemean, R=10000)
boot.ci(b1, conf = c(0.95),type = c("perc"))

#RNAcofold


b1 = boot(RNAcofold,samplemean, R=10000)
boot.ci(b1, conf = c(0.95),type = c("perc"))

###################################### TPR

Dinoknot <- DinoKnot_srna$TPR
RNAcofold <- RNAcofold_srna$TPR

### PERMUTATION TEST

#Dinoknot AND #RNAcofold

permTS(Dinoknot,RNAcofold,alternative="two.sided",method="exact.mc",control=PC) 



#### BOOT STRAPPING 

#Dinoknot

b1 = boot(Dinoknot,samplemean, R=10000)
boot.ci(b1, conf = c(0.95),type = c("perc"))

#RNAcofold


b1 = boot(RNAcofold,samplemean, R=10000)
boot.ci(b1, conf = c(0.95),type = c("perc"))

##################################### MCC



Dinoknot <- DinoKnot_srna$MCC
RNAcofold <- RNAcofold_srna$MCC

### PERMUTATION TEST

#Dinoknot AND #RNAcofold

permTS(Dinoknot,RNAcofold,alternative="two.sided",method="exact.mc",control=PC) 



######## BOOT STRAPPING 



#Dinoknot

b1 = boot(Dinoknot,samplemean, R=10000)
boot.ci(b1, conf = c(0.95),type = c("perc"))

#RNAcofold


b1 = boot(RNAcofold,samplemean, R=10000)
boot.ci(b1, conf = c(0.95),type = c("perc"))





############################################################################## SNORNA

###################################### PPV

Dinoknot <- DinoKnot_snorna$PPV
RNAcofold <- RNAcofold_snorna$PPV

### PERMUTATION TEST

#Dinoknot AND #RNAcofold

permTS(Dinoknot,RNAcofold,alternative="two.sided",method="exact.mc",control=PC) 



## BOOT STRAPPING 

#Dinoknot

b1 = boot(Dinoknot,samplemean, R=10000)
boot.ci(b1, conf = c(0.95),type = c("perc"))

#RNAcofold


b1 = boot(RNAcofold,samplemean, R=10000)
boot.ci(b1, conf = c(0.95),type = c("perc"))

###################################### TPR

Dinoknot <- DinoKnot_snorna$TPR
RNAcofold <- RNAcofold_snorna$TPR

### PERMUTATION TEST

#Dinoknot AND #RNAcofold

permTS(Dinoknot,RNAcofold,alternative="two.sided",method="exact.mc",control=PC) 



#### BOOT STRAPPING 

#Dinoknot

b1 = boot(Dinoknot,samplemean, R=10000)
boot.ci(b1, conf = c(0.95),type = c("perc"))

#RNAcofold


b1 = boot(RNAcofold,samplemean, R=10000)
boot.ci(b1, conf = c(0.95),type = c("perc"))

##################################### MCC



Dinoknot <- DinoKnot_snorna$MCC
RNAcofold <- RNAcofold_snorna$MCC

### PERMUTATION TEST

#Dinoknot AND #RNAcofold

permTS(Dinoknot,RNAcofold,alternative="two.sided",method="exact.mc",control=PC) 



######## BOOT STRAPPING 



#Dinoknot

b1 = boot(Dinoknot,samplemean, R=10000)
boot.ci(b1, conf = c(0.95),type = c("perc"))

#RNAcofold


b1 = boot(RNAcofold,samplemean, R=10000)
boot.ci(b1, conf = c(0.95),type = c("perc"))










######### 70 SAMPLE SUBSET #######################



# DINOKNOT_MAX VALUES OUT OF 400 ############

Dinoknot_MAX <- read_csv("~/srna_400_cases_TPR_MCC_PPV.csv") # read in 400 cases DinoKnot performance characteristics


MAX_PPV <- Dinoknot_MAX %>% 
  group_by(interaction) %>%
  arrange(desc(PPV)) %>%  # Arrange by descending PPV
  slice(1) %>%            # Select the first result in each group
  ungroup() %>% select(PPV)


MAX_TPR <- Dinoknot_MAX %>% 
  group_by(interaction) %>%
  arrange(desc(TPR)) %>%  # Arrange by descending PPV
  slice(1) %>%            # Select the first result in each group
  ungroup() %>% select(TPR)


MAX_MCC <- Dinoknot_MAX %>% 
  group_by(interaction) %>%
  arrange(desc(MCC)) %>%  # Arrange by descending PPV
  slice(1) %>%            # Select the first result in each group
  ungroup() %>% select(MCC)

interactions_compared <- unique(Dinoknot_MAX$interaction)

####### MFE INTERACTION SUBSET




## Dinoknot_MFE

DinoKnot_srna_subset <- DinoKnot_srna %>% filter(pair_id %in% interactions_compared)

## RNAcofold_MFE

RNAcofold_srna_subset <- RNAcofold_srna %>% filter(interaction %in% interactions_compared)




###################################### PPV

Dinoknot_MAX <- MAX_PPV$PPV
Dinoknot_MFE <- DinoKnot_srna_subset$PPV
RNAcofold <- RNAcofold_srna$PPV

### PERMUTATION TEST

#Dinoknot_MAX AND DinoKnot_MFE

permTS(Dinoknot_MAX,Dinoknot_MFE,alternative="two.sided",method="exact.mc",control=PC) 


#Dinoknot_MAX AND RNAcofold_MFE


permTS(Dinoknot_MAX,RNAcofold,alternative="two.sided",method="exact.mc",control=PC) 


###### BOOT STRAPPING 
#Dinoknot_MAX

b1 = boot(Dinoknot_MAX,samplemean, R=10000)
boot.ci(b1, conf = c(0.95),type = c("perc"))


#Dinoknot_MFE

b1 = boot(Dinoknot,samplemean, R=10000)
boot.ci(b1, conf = c(0.95),type = c("perc"))

#RNAcofold_MFE


b1 = boot(RNAcofold,samplemean, R=10000)
boot.ci(b1, conf = c(0.95),type = c("perc"))

###################################### TPR


Dinoknot_MAX <- MAX_TPR$TPR
Dinoknot_MFE <- DinoKnot_srna_subset$TPR
RNAcofold <- RNAcofold_srna$TPR

### PERMUTATION TEST

#Dinoknot_MAX AND DinoKnot_MFE

permTS(Dinoknot_MAX,Dinoknot_MFE,alternative="two.sided",method="exact.mc",control=PC) 


#Dinoknot_MAX AND RNAcofold_MFE


permTS(Dinoknot_MAX,RNAcofold,alternative="two.sided",method="exact.mc",control=PC) 


#### BOOT STRAPPING 


#Dinoknot_MAX

b1 = boot(Dinoknot_MAX,samplemean, R=10000)
boot.ci(b1, conf = c(0.95),type = c("perc"))


#Dinoknot_MFE

b1 = boot(Dinoknot,samplemean, R=10000)
boot.ci(b1, conf = c(0.95),type = c("perc"))

#RNAcofold_MFE


b1 = boot(RNAcofold,samplemean, R=10000)
boot.ci(b1, conf = c(0.95),type = c("perc"))

##################################### MCC


Dinoknot_MAX <- MAX_MCC$MCC
Dinoknot_MFE <- DinoKnot_srna_subset$MCC
RNAcofold <- RNAcofold_srna$MCC

### PERMUTATION TEST

#Dinoknot_MAX AND DinoKnot_MFE

permTS(Dinoknot_MAX,Dinoknot_MFE,alternative="two.sided",method="exact.mc",control=PC) 


#Dinoknot_MAX AND RNAcofold_MFE


permTS(Dinoknot_MAX,RNAcofold,alternative="two.sided",method="exact.mc",control=PC) 



######## BOOT STRAPPING 


#Dinoknot_MAX

b1 = boot(Dinoknot_MAX,samplemean, R=10000)
boot.ci(b1, conf = c(0.95),type = c("perc"))


#Dinoknot_MFE

b1 = boot(Dinoknot,samplemean, R=10000)
boot.ci(b1, conf = c(0.95),type = c("perc"))

#RNAcofold_MFE


b1 = boot(RNAcofold,samplemean, R=10000)
boot.ci(b1, conf = c(0.95),type = c("perc"))





