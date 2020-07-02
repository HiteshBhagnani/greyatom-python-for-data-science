# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
new_record= np.array(new_record)
#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
#print(type(data))
#print(type(new_record))
#Code starts here
census = np.concatenate((data,new_record))
print(np.shape(data))
print(np.shape(census))

age = np.array(census[:,0])
max_age = age.max()
min_age = age.min()
print(max_age)
print(min_age)
age_mean = np.mean(age)

age_std = np.std(age)
print(age_mean)
print(age_std)


race = np.array(census[:,2])
race_0  = np.extract(race==0,race)
race_1 = np.extract(race==1,race)
race_2 = np.extract(race==2,race)
race_3 = np.extract(race==3,race)
race_4 = np.extract(race==4,race)

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

length = [len_0,len_1,len_2,len_3,len_4]
minority_race = length.index(min(length))
print(minority_race)
#step4
senior_citizens= np.array(census[age>60,6])
working_hours_sum = sum(senior_citizens)
senior_citizens_len = len(senior_citizens)
avg_working_hours = working_hours_sum/senior_citizens_len

print(working_hours_sum)
print(avg_working_hours)

#step 5
education = np.array(census[:,1])
high = np.array(census[education>10,7])
low = np.array(census[education<=10,7])
print(high)
print(low)
avg_pay_high = np.mean(high)
avg_pay_low = np.mean(low)
print(avg_pay_high)
print(avg_pay_low)




