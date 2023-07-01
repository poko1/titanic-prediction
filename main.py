import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
df = pd.read_csv("titanic.csv")
X = df[['pclass', 'sex', 'fare']]
X['sex'] = X['sex'].map({'male': 0, 'female': 1})
y = df['survived']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test =  train_test_split(X,y,test_size=0.2,random_state=1)

from sklearn.ensemble import RandomForestClassifier
randf = RandomForestClassifier()
randf.fit(X_train,y_train)
pred = randf.predict(X_test)
print(classification_report(y_test,pred))

import pickle
pickle.dump(randf,open('survival_pred.pkl','wb'))