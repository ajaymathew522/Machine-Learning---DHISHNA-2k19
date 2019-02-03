from sklearn import svm
C=1.0
from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
iris_flower = datasets.load_iris()
lin_svc = svm.SVC (kernel='linear',C=C)
rbf_syn = svm.SVC (kernel='rbf',gamma=0.7,C=C)
poly_svc = svm.SVC (kernel='poly',degree=3,C=C)

X_train,X_test,y_train,y_test = train_test_split(iris_flower.data,iris_flower.target,test_size = 0.3)

lin_svc.fit(X_train,y_train)
rbf_syn.fit(X_train,y_train)
poly_svc.fit(X_train,y_train)

print(X_train)
print(y_train)
print(X_test)
print(y_test)