#from sklearn.datasets import load_iris
#from sklearn.tree import TreeClassifier
from sklearn.model_selection import train_test_split
import numpy as np 
import pandas as pd 
from sklearn.metrics import confusion_matrix 
from sklearn.tree import DecisionTreeClassifier 
from sklearn.metrics import accuracy_score 
from sklearn.metrics import classification_report

data=pd.read_csv('C:\\out\\segmented_block_2.csv')
y=data['class']
x=data.iloc[:,0:50]

#x=iris.data()
#y=iris.target()

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
tc=DecisionTreeClassifier()
tc.fit(x_train,y_train)
y_pred=tc.predict(x_test)


#clf_gini = DecisionTreeClassifier(criterion = "gini", random_state = 100,max_depth=3, min_samples_leaf=5) 
# Performing training 
#clf_gini.fit(x_train, y_train)
#y_pred=clf_gini.predict(x_test)



#clf_entropy = DecisionTreeClassifier(criterion = "entropy", random_state = 100,max_depth = 3, min_samples_leaf = 5) 
# Performing training 
#clf_entropy.fit(x_train, y_train)
#y_pred=clf_entropy.predict(x_test)


print(confusion_matrix(y_test,y_pred))
print ("Accuracy : ", accuracy_score(y_test,y_pred)*100) 
print("Report : ", classification_report(y_test, y_pred)) 
