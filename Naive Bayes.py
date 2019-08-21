import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.datasets import fetch_20newsgroups
ds = fetch_20newsgroups()
#dir(ds)
categories = ds.target_names

train = fetch_20newsgroups(subset='train', categories=categories)

test = fetch_20newsgroups(subset='test', categories=categories)

classifier = make_pipeline(TfidfVectorizer(), MultinomialNB())
classifier.fit(train.data, train.target)

pred = classifier.predict(test.data)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(test.target, pred)
plt.figure(figsize=(20,10))
sns.heatmap(cm, square=True, annot=True, xticklabels=train.target_names, fmt='d', yticklabels=train.target_names)

def new_predict(s, train=train, classifier=classifier):
    p = classifier.predict([s])
    return train.target_names[p[0]]

new_predict('turbo')