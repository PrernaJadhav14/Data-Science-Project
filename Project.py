import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#importing all the required libraries
'''group project
by Prerna 7037
and Nikhil 7085
'''
athletes = pd.read_csv('C:/Users/HP/Desktop/Project/athlete_events.csv')
regions = pd.read_csv('C:/Users/HP/Desktop/Project/noc_regions.csv')

athletes_df = athletes.merge(regions,how='left',on='NOC')#merging both the datasets since they have common column NOC
#print(athletes_df.head())
begin=athletes_df.head()
#Size of the dataset!!
print("Total size of Regions dataset is: ",regions.size)
print("Total size of Athlete dataset is: ",athletes.size)
print("Total size of aggregate of athletes and regions dataset i.e Athlete_df is: ",athletes_df.size)
#Shape of the dataset!!
print("Total numbers of rows and columns in Athlete dataset are: ",athletes.shape)
print("Total numbers of rows and columns in Region dataset are: ",regions.shape)
print("Total numbers of rows and columns in our merged dataset are :",athletes_df.shape)
#Shape of the dataset!!
print("The null values in datasets are:",athletes_df.isnull().sum())
#Dealing with null value of column "Age"
print("The null value in Age column are:",athletes_df.Age.isnull())
print("The null value in Age column are:",athletes_df["Age"].fillna(athletes_df.Age.mode()).head(20))
#Dealing with null value of column "Weight"
print("The null value in Weight column are:",athletes_df.Weight.isnull())
print("After filling the age columns null values with average of age:",athletes_df["Weight"].fillna(athletes_df.Weight.mean()))
#Dealing with null value of column "Height"
print(athletes_df.Height.head(20))
print("The null value in Height column are:",athletes_df.Height.isnull())
print("After filling the Height column :",athletes_df["Height"].fillna(athletes_df.Height.mean()).head(20))
#Dealing with null value of column "Medal"
print("The null value in Medal column are:",athletes_df.Medal.isnull())
print("The null value after filling with padding method in Medal column are:",athletes_df["Medal"].fillna(method ='pad').head(20))
#Dealing with null value of column "Region"
print("The null value in region column are:",athletes_df.region.isnull())
print("After filling the region column :",athletes_df["region"].fillna(athletes_df.region.mode()).head(20))
#Dealing with null value of column "Notes"
print("The null value in notes column are:",athletes_df.notes.isnull())
print("After filling the notes column :",athletes_df["notes"].fillna(0).head(20))


print(begin.describe)#coninue the file statemepip
Womply=athletes_df[(athletes_df.Sex == 'F') & (athletes_df.Season == 'Summer')]
Menply=athletes_df[(athletes_df.Sex == 'M') & (athletes_df.Season == 'Summer')]
Men = Menply.groupby('Year')['Sex'].value_counts()
part = Womply.groupby('Year')['Sex'].value_counts()
plt.figure(figsize=(12,6))
part.loc[:,'F'].plot(label="Female Participation",color="r" ,marker="o",markerfacecolor='y')
Men.loc[:,'M'].plot(label="Male Participation",color="g" ,marker="o",markerfacecolor='b')
plt.ylabel("Participants",fontweight = 'bold')
plt.xlabel("Years",fontweight = 'bold')
plt.title("Plot of female and Male Athletes over time",fontweight = 'bold')
plt.tick_params(axis = 'both',width=2,length = 10, direction ='inout',color ='r',pad =4 ,rotation = 2)
plt.legend(facecolor="y",shadow=True)
plt.show()
top_10_countries= athletes_df.Team.value_counts().sort_values(ascending=False).head(10)#most number of participants participating
print(top_10_countries)
plt.figure(figsize=(12,6))
plt.tick_params(axis ='both',length = 10, direction='inout',color ='r',pad =2 ,rotation = 2,width=2)
plt.xlabel('Nations',color='blue',fontweight = 'bold')
plt.ylabel('Participation',color='blue',fontweight = 'bold')
plt.title("Overall Participation of the top 10 countries",fontweight = 'bold')
value1= plt.annotate('17847',xy=(0,1.793),xytext=(0,1.818e+04),fontsize=10,fontweight = 'bold')
value2= plt.annotate('11988',xy=(9,6.76),xytext=(1,1.236e+04),fontsize=10,fontweight = 'bold')
value3= plt.annotate('11404',xy=(2,1.06),xytext=(2,1.167e+04),fontsize=10,fontweight = 'bold')
value4= plt.annotate('10260',xy=(3,2.57),xytext=(3,1.057e+04),fontsize=10,fontweight = 'bold')
value5= plt.annotate('9326',xy=(4,2.54),xytext=(4,9.58e+03),fontsize=10,fontweight = 'bold')
value6= plt.annotate('9279',xy=(5,0.62),xytext=(5,9.47e+03),fontsize=10,fontweight = 'bold')
value7= plt.annotate('8289',xy=(6,-2.79),xytext=(6,8.52e+03),fontsize=10,fontweight = 'bold')
value8= plt.annotate('8052',xy=(1,-0.81),xytext=(7,8.23e+03),fontsize=10,fontweight = 'bold')
value9= plt.annotate('7513',xy=(2,-0.58),xytext=(8,7.79e+03),fontsize=10,fontweight = 'bold')
value10= plt.annotate('6547',xy=(2,-0.58),xytext=(9,6.95e+03),fontsize=10,fontweight = 'bold')
#plt.grid(axis='y',color = 'black', linestyle = '--', linewidth = 1)
plt.tick_params(axis = 'both',width=2,length = 10, direction ='inout',color ='g',pad =4 ,rotation = 2)
sns.barplot(x=top_10_countries.index,y=top_10_countries,edgecolor ='black')
plt.show()
#histogram for age of athletes
plt.figure(figsize=(12,6))
plt.title("Age distrubution of the athletes",fontweight = 'bold')
plt.xlabel('Age of athletes',fontweight = 'bold')
plt.ylabel('Number of Participants',fontweight = 'bold')
plt.grid(axis='y',color = 'black', linestyle = '--', linewidth = 1)
plt.hist(athletes_df.Age, bins=np.arange(10,80,2) ,color='orange',edgecolor ='blue')
plt.tick_params(axis = 'both',width=2,length = 10, direction ='inout',color ='r',pad =4 ,rotation = 2)
plt.show()
winter_sports=athletes_df[athletes_df.Season=='Winter'].Sport.unique()#So olympics has winter olympic and summer olympic
#so to mention particular games in winter olympics we use this
print(winter_sports)

summer_sports=athletes_df[athletes_df.Season=='Summer'].Sport.unique()
print(summer_sports)


#pie chart
gender_counts = athletes_df.Sex.value_counts()#to count total number of Male athletes and female athletes
print(gender_counts)
plt.figure(figsize=(12,6))
mylabels=['Male','Females']
col=['cyan','yellow']
myexplode = [0.05,0.1]
plt.title("Participation rate on basis of gender",fontweight = 'bold')
plt.pie(gender_counts,labels=mylabels,autopct=('%1.1f%%'),startangle=0,colors=col,center=(0,0),
        rotatelabels=False,pctdistance=0.7,shadow=True,explode=myexplode)
plt.show()
