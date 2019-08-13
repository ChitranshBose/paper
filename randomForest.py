from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import numpy as np 
import pandas as pd 
from sklearn.metrics import confusion_matrix 
#from sklearn.tree import DecisionTreeClassifier 
from sklearn.metrics import accuracy_score 
from sklearn.metrics import classification_report

data=pd.read_csv('C:\\out\\segmented_block.csv')
y=data['class']
x=data.iloc[:,0:50]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
#tc=DecisionTreeClassifier()
rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)
rf.fit(x_train,y_train)
y_pred=tc.predict(x_test)

print(confusion_matrix(y_test,y_pred))
print ("Accuracy : ", accuracy_score(y_test,y_pred)*100) 
print("Report : ", classification_report(y_test, y_pred))
