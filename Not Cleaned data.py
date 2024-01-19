#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import os
import email
import email.policy
import re
from bs4 import BeautifulSoup
from sklearn.ensemble import IsolationForest
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import roc_auc_score
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import precision_score, recall_score, accuracy_score
from sklearn.metrics import roc_auc_score, accuracy_score, f1_score, precision_score, recall_score, confusion_matrix
#from sklearn.ensemble import GradientBoostingClassifier

#Let's explore the directory segmentation
os.listdir('D:/4-1/research/email datasets/ham and spam')


# In[3]:


ham_files = [name for name in sorted(os.listdir('D:/4-1/research/email datasets/ham and spam/ham/')) if len(name) > 20]
spam_files = [name for name in sorted(os.listdir('D:/4-1/research/email datasets/ham and spam/spam')) if len(name) > 20]


# In[4]:


print('Amount of ham emails: ',len(ham_files))
print('Amount of spam emails: ',len(spam_files))
print('Spam percentage: ',100*(len(spam_files)/(len(ham_files)+len(spam_files))),'%')


# In[5]:


#Let's load an email to see how it looks like:

#Using email.parser: https://docs.python.org/3/library/email.parser.html
#"The email package provides a standard parser that understands most email document structures, including MIME documents"

with open(os.path.join('D:/4-1/research/email datasets/ham and spam/ham/', ham_files[0]), "rb") as file:
    ham_email =  email.parser.BytesParser(policy=email.policy.default).parse(file)

print('Header field names: ',ham_email.keys())
print('\n -------------------------------------- \n')
print('Message field values: ',ham_email.values())
print('\n -------------------------------------- \n')
print('Message content:',ham_email.get_content()[:500])


# In[6]:


#Let's extract some email fields

e_subject = ham_email.get_all('Subject')
e_from = ham_email.get_all('From')
e_to = ham_email.get_all('To')

print('Email from: ',e_from)
print('Email to: ',e_to)
print('Email subject: ',e_subject)


# Data Importing
# 
# Now that we've explored how the data is structured, we are going to import all emails to be processed later on the notebook.

# In[7]:


def upload_ham_emails(filename):
     """This function process a ham email file located at a specified directory and returns it as an email object"""
     directory = 'D:/4-1/research/email datasets/ham and spam/ham/'
     with open(os.path.join(directory, filename), "rb") as file:
      return email.parser.BytesParser(policy=email.policy.default).parse(file)
    
def upload_spam_emails(filename):
     """This function process a spam email file located at a specified directory and returns it as an email object"""
     directory = 'D:/4-1/research/email datasets/ham and spam/spam/'
     with open(os.path.join(directory, filename), "rb") as file:
       return email.parser.BytesParser(policy=email.policy.default).parse(file)
    
ham_emails = [upload_ham_emails(filename=name) for name in ham_files]
spam_emails = [upload_spam_emails(filename=name) for name in spam_files]
 


# In[8]:


#Checking if everything was uploaded properly:

print(ham_emails[0].get_all('Subject'))
print(ham_emails[0].get_all('From'))
print(ham_emails[0].get_all('To'))
print(ham_emails[0].get_all('Date'))
print(ham_emails[0].get_content())
print('\n\n -----------------------------------------------------------\n\n')
print(spam_emails[1].get_all('Subject'))
print(spam_emails[1].get_all('From'))
print(spam_emails[1].get_all('To'))
print(spam_emails[1].get_all('Date'))
print(spam_emails[1].get_content())


# In[9]:


#Let's research about what email content types are:

ham_content_types = []
spam_content_types = []

for i in range(len(ham_files)):
    ham_content_types.append(ham_emails[i].get_content_type())

for i in range(len(spam_files)):
    spam_content_types.append(spam_emails[i].get_content_type())

print('Ham content types: ',set(ham_content_types))
print('Spam content types: ',set(spam_content_types))


# Converting emails to plain text In the previous output you could notice that there are some emails with HTML format. We need them to be plain text format.

# In[10]:


def email_content_type(email):
    """This function returns the content type of an email and if it has a multipart shape then returns the multiparts type"""
    if isinstance(email, str):
        return email
    payload = email.get_payload()
    if isinstance(payload, list):
        return "multipart({})".format(", ".join([email_content_type(sub_email) for sub_email in payload]))
    else:
        return email.get_content_type()


# In[11]:


ham_content_types = []
spam_content_types = []

for i in range(len(ham_files)):
    ham_content_types.append(email_content_type(ham_emails[i]))

for i in range(len(spam_files)):
    spam_content_types.append(email_content_type(spam_emails[i]))

print('Ham content types: ',set(ham_content_types))
print('Spam content types: ',set(spam_content_types))


# In[14]:


#Now that we've identified what are the email content types, we need to transform all html emails to plain format.

from bs4 import BeautifulSoup
html = spam_emails[1].get_content()
soup = BeautifulSoup(html)
print(soup.get_text().replace('\n\n',''))


# In[15]:


#Let's build a function with the previous process to convert all html emails into plain text

def html_to_plaintext(email):
    soup = BeautifulSoup(email.get_content())
    return soup.get_text().replace('\n\n','').replace('\n',' ') 


# In[16]:


#Now all emails which have/contain HTML tags will be converted to plain text

def email_to_plaintext(email):
    content_type = email_content_type(email)
    for part in email.walk(): 
        #The .walk() documentation at https://docs.python.org/3/library/email.message.html
        #"The walk() method is an all-purpose generator which can be used to iterate over all 
        #the parts and subparts of a message object tree, in depth-first traversal order."
        partContentType = part.get_content_type()
        if partContentType not in ['text/plain','text/html']:
            continue
        try:
            partContent = part.get_content()
        except: 
            partContent = str(part.get_payload())
        if partContentType == 'text/plain':
            return partContent
        else:
            return html_to_plaintext(part)


# In[17]:


#Let's test this out.
email_test1 = email_to_plaintext(spam_emails[1])
email_test2 = email_to_plaintext(spam_emails[227])
print(email_test1)
print('\n\n')
print(email_test2[:1000])


# In[18]:


#Spam email #226 contains an unknown encoding so we will remove it from the list
del spam_emails[226]


# Building the dataset to train the model Essentially we'll create a dataframe with the emails' content and their particular label. This will allow us to implement NLP to feed a ML model

# In[19]:


ham_dataset = []
spam_dataset = []

#Ham processing
for i in range(len(ham_emails)):
    ham_dataset.append(email_to_plaintext(ham_emails[i]))
ham_dataset = pd.DataFrame(ham_dataset,columns = ['Email content'])
ham_dataset['Label'] = 0


#Spam processing
for i in range(len(spam_emails)):
    spam_dataset.append(email_to_plaintext(spam_emails[i]))
spam_dataset = pd.DataFrame(spam_dataset,columns=['Email content'])
spam_dataset['Label'] = 1
dataset = pd.concat([ham_dataset,spam_dataset])
dataset.head()


# In[20]:


#We will shuffle the data and also reset indexes
dataset = dataset.dropna()
dataset = dataset.sample(frac=1).reset_index(drop=True)
dataset.head()


# In[21]:


from sklearn.model_selection import train_test_split
x=dataset['Email content']
y=dataset['Label']

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)


# In[22]:


#checking if everything went OK.
print ('X_train: ',len(X_train))
print('X_test: ',len(X_test))
print('Y_train: ',len(y_train))
print('Y_test: ',len(y_test))


# Using MultiNomial Naive Bayes as the Model with CountVectorizer

# In[23]:


from sklearn.naive_bayes import MultinomialNB
model = MultinomialNB()
vect = CountVectorizer(min_df=5,ngram_range=(2,5)).fit(X_train)
X_train_vectorized = vect.transform(X_train)
X_test_vectorized = vect.transform(X_test)
model.fit(X_train_vectorized, y_train)


# In[24]:


y_pred = model.predict(X_test_vectorized)


# Check Accuracy,Precision,recall and F1 score

# In[25]:


print("Precision: {:.2f}%".format(100 * precision_score(y_test, y_pred)))
print("Accuracy: {:.2f}%".format(100 * accuracy_score(y_test, y_pred)))
print("Recall: {:.2f}%".format(100 * recall_score(y_test, y_pred)))
print("F1 score: {:.2f}%".format(100 * f1_score(y_test, y_pred)))


# Check the Confusion Matrix

# In[26]:


from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
cm


# Plot the confusion matrix

# In[28]:


import matplotlib.pyplot as plt
import seaborn as sns

matrix_df = pd.DataFrame(cm, index=["Ham", "Spam"], columns=["Ham", "Spam"])
df = matrix_df.astype('float')/matrix_df.sum(axis=1)[:, np.newaxis]
sns.heatmap(df, annot=True)
plt.show()


# SVC with Countvectorizer

# In[29]:


from sklearn.svm import LinearSVC
cv_SVC_Count=CountVectorizer()
x_SVC_Count=cv_SVC_Count.fit_transform(x)
X_train,X_test,y_train,y_test=train_test_split(x_SVC_Count,y,test_size=0.2)
model_SVC_Count=LinearSVC(C=1000, dual=False)
y_predict_SVC_Count=model_SVC_Count.fit(X_train,y_train)
y_pred = y_predict_SVC_Count.predict(X_test)


# Check Accuracy,Precision,recall and F1 score

# In[30]:


print("Precision: {:.2f}%".format(100 * precision_score(y_test, y_pred)))
print("Accuracy: {:.2f}%".format(100 * accuracy_score(y_test, y_pred)))
print("Recall: {:.2f}%".format(100 * recall_score(y_test, y_pred)))
print("F1 score: {:.2f}%".format(100 * f1_score(y_test, y_pred)))


# Check the Confusion Matrix

# In[31]:


cm1 = confusion_matrix(y_test, y_pred)
cm1


# Plot the confusion matrix

# In[32]:


matrix_df = pd.DataFrame(cm1, index=["Ham", "Spam"], columns=["Ham", "Spam"])
df = matrix_df.astype('float')/matrix_df.sum(axis=1)[:, np.newaxis]
sns.heatmap(df, annot=True)
plt.show()


# In[ ]:




