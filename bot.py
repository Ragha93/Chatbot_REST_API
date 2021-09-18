from flask import Flask, jsonify, request
import numpy as np
import pandas as pd
import string,nltk,re,pickle
from nltk.stem import WordNetLemmatizer
from sklearn.pipeline import Pipeline

#Loading Pickle file
with open('C:\\Users\\raghavendra.s.k\\Desktop\\Files\\Flask\\pipe.pkl', 'rb') as file:
  model = pickle.load(file)

#Dictionary to get responses
def data_dict():
  return {0:'Hello! how can i help you ?',1:'I am your virtual learning assistant',2:'I hope I was able to assist you, Good Bye',
             3:'Link: Machine Learning wiki',4:'Link: Neural Nets wiki',5:'Link: Olympus wiki',6:'Please use respectful words',
             7:'Transferring the request to your PM'}

#Preprocessing input message
def preprocess(x):
  WNL = WordNetLemmatizer()
  data = data_dict()
  pred = model.predict([" ".join([WNL.lemmatize(i) for i in "".join([i for i in re.sub("<.*>|[\s]{2,}| [.0-9]+| [.0-9]{2,10}|[^a-zA-Z]"," ",x.lower()) if i not in string.punctuation]).split(" ")])])
  x = data[pred[0]]
  return x,pred


app = Flask(__name__)
@app.route('/', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'):
        data = "Hello!!! Welcome to Arattai Kanini"
        return jsonify({'data': data})

@app.route('/chat/<string:i>', methods = ['GET'])
def disp(i):
    print(i)
    i = i.lower()
    if (i== 'end' or i=='quit'):
      resp_text = "\nThanks for connecting"
    else:
      x,y = preprocess(i)
      resp_text = x
    return jsonify({'data': resp_text})


# driver function
if __name__ == '__main__':
    app.run(host="192.168.0.100",port=1993, threaded=True,debug = True)
