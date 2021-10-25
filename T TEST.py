# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 12:13:15 2021

@author: ashle
"""

#packages
import pandas as pd
from scipy.stats import shapiro 
from matplotlib import pyplot
import scipy.stats as stats
from scipy.stats import ttest_ind

# dataframe 
diabetes = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Datasets/Diabetes/DB1_Diabetes/diabetic_data.csv')

# Sample of dataframe
diabetes_small = diabetes.sample(100)

## Generate list of var names
list(diabetes_small)

diabetes['totalCountProcedures'] = diabetes['num_lab_procedures'] + diabetes['num_procedures']

## T TEST

# 1. Is there a difference between sex (M:F) and the number of lab procedures performed?
# Gender and Total Count Procedures

list(diabetes)

Female = diabetes[diabetes['gender']=='Female']
Male = diabetes[diabetes['gender']=='Male']

ttest_ind(Female['totalCountProcedures'], Male['totalCountProcedures'])

## Ttest_indResult(statistic=-0.6747218803792331, pvalue=0.4998540133474586)
## There is not a difference between the average number of procedures 
## between males and females due to the P-value being greater than 0.05 
##meaning that we fail to reject the null hypothesis.


# 2. Is there a difference between gender (M:F) and the number of days in hospital?
# Gender and number of days in the hospital 

list(diabetes)
Female = diabetes[diabetes['gender']=='Female']
Male = diabetes[diabetes['gender']=='Male']
ttest_ind(Female['time_in_hospital'], Male['time_in_hospital'])

## Ttest_indResult(statistic=9.542637042242887, pvalue=1.4217299655114968e-21)
## There a difference between the average time in hospital for males and females
## due to the P-value is less than 0.05 
## meaning that we successfully reject the null hypothesis.
 
# 3. Is there a difference between RACE (Caucasian and African American) and the number of days in hospital?
# Race and time in the hospital

list(diabetes)
Caucasian = diabetes[diabetes['race']=='Caucasian']
AfricanAmerican = diabetes[diabetes['race']=='AfricanAmerican']
ttest_ind(Caucasian['time_in_hospital'], AfricanAmerican['time_in_hospital'])

## Ttest_indResult(statistic=-5.0610017032095325, pvalue=4.178330085585203e-07)
## There is a difference between time in hospital with African Americans and Cacasians
## We see that the P-Value is less than 0.05 so we can successfully reject the null hypothesis.

#4. Is there a difference between RACE (Caucasian and African American) and the number
# of lab procedures performed?
# RACE and NUMBER LAB PROCEDURES PERFORMED

list(diabetes)
Caucasian = diabetes[diabetes['race']=='Caucasian']
AfricanAmerican = diabetes[diabetes['race']=='AfricanAmerican']
ttest_ind(Caucasian['totalCountProcedures'], AfricanAmerican['totalCountProcedures'])

## Ttest_indResult(statistic=-6.98407655628912, pvalue=2.8860334493798807e-12)
## There is a difference with the number of lab procedures for African Americans and Caucasians
##since the P-value is less than 0.05 we can reject the null hypothesis.