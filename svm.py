import sklearn
#from sklearn.svm import svc
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd

print("starting to read...")
data=pd.read_csv(r'C:\Users\lenovo\Desktop\test.csv')
y=data['status']
x=data.iloc[:,0:3]

print("analysing...")
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)
svm=svm.SVC(kernel='linear')--
#sc=StandardScaler()
#sc.fit(x_train)
#x_train=sc.transform(x_train)
#x_test=sc.transform(x_test)
svm.fit(x_train,y_train)
y_pred=svm.predict(x_test)

print("about to show...")
print(confusion_matrix(y_test,y_pred))
print ("Accuracy : ", accuracy_score(y_test,y_pred)*100) 
print("Report : ", classification_report(y_test, y_pred))
