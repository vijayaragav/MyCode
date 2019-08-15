import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
df=pd.read_csv('C:\\Users\\HP\\Downloads\\Dataset\\titanic.csv')


tit = df.drop(['PassengerId','Name', 'SibSp', 'Parch', 'Cabin', 'Ticket', 'Embarked'], axis='columns')
tit['Age'].fillna('25', inplace=True)
le_Sex = LabelEncoder()
tit['Sex_n'] = le_Sex.fit_transform(tit['Sex'])
#print(tit.head())
X = tit.drop(['Survived', 'Sex'], axis='columns')
Y = tit.drop(['Pclass','Sex', 'Age', 'Sex_n', 'Fare'], axis='columns')
#print(X.head())


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

clf=DecisionTreeClassifier(criterion='entropy', max_depth=3)
clf.fit(X_train, Y_train)

clf.score(X_test, Y_test)

clf.predict([[2,45,9.0,1]])