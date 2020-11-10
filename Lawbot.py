import nltk
import string
import numpy as numpy
#import pandas as pandas
import random
import sklearn
from sklearn.feature_extraction.text import TfidVectorizer
from sklearn.metrics.pairwise import cosine_similarity

doc=open("C:\Users\hp\Desktop\Chatbot\AI.txt")
laws=doc.read()

laws=laws.lower()
#One line download them
nltk.download('punkt')

#Similar first time use
nltk.download('wordnet')

#Place the data into sentenses
sentense_tokens=nltk.sent_tokenize(laws)

#The data into list of words
word_tokens=nltk.word_tokenize(laws)



sentense_tokens[:2]
[
    'Techniques of knowledge representation There are mainly four ways of knowledge representation which are given as follows:'
]
word_tokens[:2]
['Technique','of','knowledge','represantation']



ltz=nltk.stem.WordLemmatizer()

def  ltokens(tokens):
    return[ltz.lemmatize(tokens) for token in tokens]

    remove_punctuation_diction=dict((ord(punct),None) for punct in string.punctuation)

    def Lmnormalize(text):
        return ltokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_diction)))


#Greeting text available for soothing and make it fun
input=('Mambo','Habari','sasa','hey','greetings',"what's up",'hello')
robot_response=['Poa','Mzuri,waambaje?' 'fiti','hey','hi there','I am fine,be glad your talking to me','I am supper excited']

def greetings(sentenses):
    for word in sentense.split():
        if word.lower() in input:
            return random.choice(robot_response)

    
#How to write response
def answers(User_resp):
    chatbot_response=' '
    sentense_tokens.append(User_resp)

    vectorizer=TfidVectorizer(tokenizer = Lmnormalize,stop_words='english')
    tfidf=vectorizer.fit_transform(sentense_tokens)
    vals=cosine_similarity(tfidf[-1],tfidf)
    flaten=vals.flatten()
    flaten.sort()
    req_tfidf=flaten[-2]
    if(req_tfidf==0):
        chatbot_response=chatbot)_response+"Sorry i dont have an idea about that rule"



#using boolean functions to stop or start your conversation
flag=True
print('My name is Robottresponder! I can chart and help you know your countries rule.If you want to quit ,just type Bye!!')
while(flag==True):
    User_resp=input()
    User_resp=User_resp.lower()

    if(User_resp!='bye'):
        if(User_resp=='Thanks'  or  User_resp=='Thank you'):
            flag=False
            print('Robot_responder: Anytime dear!')
        else:
            if(greetings(User_resp)!=None):
                print('Robotresponder: '+greetings(User_resp))
            else:
                print('Robotresponder: ',end=' ')
                print(answers(User_resp))
                sentense_tokens.remove(User_resp)

    else:
            flag=False
            print('ResponderBot : Thanks for questioning me,Bye have a goodday!')
