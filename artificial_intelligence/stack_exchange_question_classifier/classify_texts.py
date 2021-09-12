from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB
from xgboost import XGBClassifier

import os
import json
import pandas as pd

basePath = os.path.dirname(os.path.abspath(__file__))

def compare_three_text_classifiers_tfidf(X,y):

    """ Run text classification for MNB, Logistic Regression and XGBoost.


    Args:
    X   (list): Features
    y   (list): target

    Returns:
    accuracies          (list): accuracy scores for each model
    models              (list): instantiated models
    tf_idf_vectorizer   (list): tf-idf vectorizer instance
    """

    #print(f'this is X {X} \n and here is y: {y}')

    # use english stop words
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')

    # generate tf-idf vectors for corpus
    X_vectorized = tfidf_vectorizer.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X_vectorized,
                                                        y,
                                                        test_size=0.25)

    # fit models
    mnb = MultinomialNB().fit(X_train, y_train)
    lr = LogisticRegression().fit(X_train, y_train)
    xgb = XGBClassifier(objective='multi:softmax').fit(X_train, y_train)

    models = [mnb, lr, xgb]

    predictions = [model.predict(X_test) for model in [mnb, lr, xgb]]

    accuracies = [accuracy_score(y_test, pred) for pred in predictions]

    for model_name, acc in zip(['Multionmial Naive Bayes','LogReg','XGB'], accuracies):

        print('le accuracy from '+model_name+f': {acc}')

    return accuracies, models, tfidf_vectorizer

if __name__ == '__main__':

    # Data preprocessing
    data = []
    with open(basePath+'/training.json', 'r') as f_in:
        for line in f_in:
            try:
                data.append(json.loads(line))
            except:
                continue    # ignore the error

    # remove the number at the beginning of the json
    data = data[1:]

    df = pd.DataFrame(data)

    # use both question and excerpt for classification
    df['concatenated'] = df[['question','excerpt']].agg(' '.join, axis=1)

    # convert dataframe strings into list of strings, change if there are other names
    X, y = df['concatenated'].tolist(), df['topic'].tolist() # alternatively use df['excerpt'] for more text?

    # retrieve accuracies from models based on splitting the training data
    accuracies, models, tfidf_vectorizer = compare_three_text_classifiers_tfidf(X,y)

    ### Hackerrank part with input data ###
    """# fit on entire training data
    mnb = MultinomialNB().fit(tfidf_vectorizer.fit_transform(X),y) 

    ### Deal with new incoming messages / Hackerrank input ###
    new_docs = []

    # insert new incoming files, first number of files
    for _ in range(int(input())):
        # insert only text of questions for input into model
        new_docs.append(json.loads(input())['question'])# alternatively use df['excerpt'] for more text?
        
    new_vectors = tfidf_vectorizer.transform(new_docs)

    # unpack and separate predictions for new input by newline
    #print(*mnb.predict(new_vectors), sep='\n')
    # this is the length of the output
    print(len(mnb.predict(new_vectors)))"""