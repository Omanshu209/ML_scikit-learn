import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestRegressor 

df=pd.read_csv('who.csv') 
df.dropna(inplace= True)
df['Developed Country']=df['Status']=='Developed'
df2=df.drop(['Status','Country'],axis=1).copy()

#for col in df2.columns:
#	print(col)

#arr=[[Year,Adult Mortality,infant deaths,Alcohol,percentage expenditure,Hepatitis B,Measles,BMI,under-five deaths,Polio,Total expenditure,Diphtheria,HIV/AIDS,GDP,Population,thinness  1-19 years,thinness 5-9 years,Income composition of resources,Schooling,Developed Country]]
#example : [2005 34.0 7 1.07 5.064688968 96.0 19 13.9 9 96.0 2.97 96.0 1.6 276.75896 39697.0 9.4 9.5 0.0 5.4 False]

#corr_matrix=df2.corr() 
#print(corr_matrix['Life expectancy '].sort_values(ascending=False))

#corresponding matrix output:

#Life expectancy                    1.000000
#Schooling                          0.727630
#Income composition of resources    0.721083
# BMI                               0.542042
#Developed Country                  0.442798
#GDP                                0.441322
#percentage expenditure             0.409631
#Alcohol                            0.402718
#Diphtheria                         0.341331
#Polio                              0.327294
#Hepatitis B                        0.199935
#Total expenditure                  0.174718
#Year                               0.050771
#Population                        -0.022305
#Measles                           -0.068881
#infant deaths                     -0.169074
#under-five deaths                 -0.192265
# thinness 5-9 years               -0.457508
# thinness  1-19 years             -0.457838
# HIV/AIDS                         -0.592236
#Adult Mortality                   -0.702523
#Name: Life expectancy , dtype: float64


X=df2.drop('Life expectancy ',axis=1).copy().values 
y=df2['Life expectancy '].copy().values
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=209)

model=RandomForestRegressor() 
model.fit(X_train,y_train)
print(model.score(X_test,y_test)) #0.9533888044330697
#print(model.predict(X_test[:10]))
#print(y_test[:10])
